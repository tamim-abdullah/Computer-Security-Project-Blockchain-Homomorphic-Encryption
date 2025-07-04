// contracts/EHRBlockchain.sol

pragma solidity ^0.8.0;

contract EHRBlockchain {
    mapping(address => string) public ehrDataHashes;

    // Function to store the encrypted data hash in the blockchain
    function storeEHRDataHash(string memory dataHash) public {
        ehrDataHashes[msg.sender] = dataHash;
    }

    // Function to get the stored data hash
    function getEHRDataHash(address user) public view returns (string memory) {
        return ehrDataHashes[user];
    }
}
