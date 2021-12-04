pragma solidity >=0.6.0 <0.9.0;
// SPDX-License-Identifier: MIT

contract SimpleStorage{
    uint favoriteNumber;

    function store(uint _favoritenum) public {
        favoriteNumber = _favoritenum;
    }

    function retreive() public view returns(uint){
        return favoriteNumber;
    }
}