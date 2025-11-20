*** Settings ***

Resource resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***

Register With Valid Username And Password
    Input Credentials   karri  salasana123
    Output Should Contain  User  Registered


*** Keywords ***
Create User And Input Login Command
    Create User  karri salasana123
    Input Login Command


