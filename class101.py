import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,'rb')as f:
              dbx.files_upload(f.read(),file_to)
        #f=open(file_from,'rb')
def main ():
    access_token='SdTrBc6lEckAAAAAAAAAAavk4mBdMyHcbq15wvVuhquwH7wlQuPNATE0hzmzrhC0'
    transferData=TransferData(access_token)

    file_from=input('enter the file path to transfer: ')
    file_to=input('enter the full path to upload to  dropbox: ')

    transferData.upload_file(file_from,file_to)
    print('file has been moved')

main()  
        