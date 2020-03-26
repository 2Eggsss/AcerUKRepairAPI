import requests
import json
url = "https://uk.answers.acer.com/ci/ajaxCustom/getCaseStatusResults"
identifier = input("Input Acer UK Case ID or Serial Number or SNID: ")
data = {"textToSearch": identifier}

requestData = (requests.post(url, data).text)
requestDatajson = json.loads(requestData)

if ((requestDatajson['success']) == False):
    print("The request sent was not successful. (Incorrect Case ID/Serial Number/SNID?)")
elif ((requestDatajson['success']) == True):
    ApprovedOrRejected = (requestDatajson['data']['ApprovedRejectedFlag'])
    Carrier = (requestDatajson['data']['Carrier'])
    CaseDate = requestDatajson['data']['CaseDate']
    CaseID = requestDatajson['data']['CaseId']
    IsInfoCase = requestDatajson['data']['IsInformationCase']
    AttachmentSend = requestDatajson['data']['IsSendAttachment']
    PreApprovalCaseID = requestDatajson['data']['PreApprovalCaseId']
    RequestID = requestDatajson['data']['RequestId']
    ShipToDate = requestDatajson['data']['ShipToDate']
    Status = requestDatajson['data']['Status']
    StatusID = requestDatajson['data']['StatusId']
    StatusUpdateDate = requestDatajson['data']['StatusUpdationDate']
    TrackingNumber = requestDatajson['data']['TrackingNumber']
    ZipCode = requestDatajson['data']['ZipCode']
    Title = requestDatajson['data']['title']

    print("\n")
    print(Title)
    print("Last Updated: " + StatusUpdateDate)
    print("Current Status: " + Status)
    print("-"*10)
    if ((ApprovedOrRejected) == ''):
        ApprovedOrRejected2 = "Unknown"
    elif ((ApprovedOrRejected).lower() == "approved"):
        ApprovedOrRejected2 = "Approved"
    elif ((ApprovedOrRejected).lower() == "rejected"):
        ApprovedOrRejected2 = "Rejected"

    print("Case Approved: " + ApprovedOrRejected2)
