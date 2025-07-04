import { Component, OnInit } from '@angular/core';
import { IPFSHTTPClient } from 'ipfs-http-client/dist/src/types';
import { DoctorService } from 'src/admin/services/doctor.service';

@Component({
  selector: 'doctor-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.sass'],
})
export class AddComponent implements OnInit {
  model: any = {
    docID: '0xB91e7Ec3765E1fdab06b9b3219134A7B5BBeE598',
    fName: 'test_name',
    lName: 'test_name',
    Doj: '',
    emailID: 'test_name@mail.com',
    phone: '123456789',
    city: 'city',
    state: 'state',
    specialty: 'specialty',
    imageHash: '',
  };

  image_url: any;
  show: boolean = false;
  msg_text: string = '';
  warn: boolean = false;
  success: boolean = false;

  ipfs: IPFSHTTPClient;

  constructor(private ds: DoctorService) {
    this.ipfs = ds.ipfs;
  }

  ngOnInit(): void {
    this.ipfs = this.ds.ipfs;
  }

  onAddDocSubmit() {
    // Validate docID
    if (!this.model.docID || this.model.docID.length < 5) {
      this.warn = true;
      this.msg_text = 'Invalid Doctor ID';
      return; // Prevent further execution if validation fails
    }

    // Proceed with the rest of the logic if docID is valid
    this.show = true;
    this.msg_text = 'Adding Doctor to the Network....';
    this.warn = false;
    this.success = false;

    // Check if image is available and upload to IPFS
    if (this.image_url) {
      this.uploadImageToIPFS(this.image_url)
        .then((imageHash) => {
          // Set the imageHash after upload
          this.model.imageHash = imageHash;
          // Add doctor info to blockchain or server (assume addDoctor method exists)
          this.ds.addDoctor(this.model.docID, this.model).then((r: any) => {
            this.success = true;
            this.msg_text = 'Data added to IPFS...';
            this.msg_text += '<br>User Added to the Blockchain';
            console.log('User added Successfully');

            this.model = {}; // Clear the form after success
          }).catch((er: any) => {
            this.warn = true;
            this.msg_text = 'Adding Doctor Failed';
            console.log(er);
          });
        })
        .catch((err) => {
          this.warn = true;
          this.msg_text = 'Error uploading image to IPFS: ' + err;
          console.log(err);
        });
    } else {
      this.warn = true;
      this.msg_text = 'Please select an image for the doctor.';
    }
  }

  // Function to upload image to IPFS
  uploadImageToIPFS(image: any): Promise<string> {
    return new Promise((resolve, reject) => {
      const file = new File([image], 'image.jpg', { type: 'image/jpeg' });

      // Upload the image to IPFS
      this.ipfs.add(file)
        .then((result: any) => {
          if (result && result.path) {
            resolve(result.path); // Return IPFS hash of the image
          } else {
            reject('Failed to upload image to IPFS');
          }
        })
        .catch((err: any) => {
          reject('Error uploading image to IPFS: ' + err.message || err);
        });
    });
  }

  // Preview selected image
  PreviewImage(event: any) {
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();
      reader.onload = (event: any) => {
        this.image_url = event.target.result;
      };
      reader.readAsDataURL(event.target.files[0]);
    }
  }

  onClose() {
    this.show = false;
    this.warn = false;
  }
}
