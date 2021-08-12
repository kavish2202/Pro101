import dropbox
import os

class Uploadfiles:
    def __init__ (self,access_token):
        self.access_token = access_token

    def paths_file(self,local_path,file_from,file_to,relative_path,dropbox_path):
        for root, dirs , files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)

    def upload_file(self,file_from,file_to,dropbox_path):
            kk = dropbox.Dropbox(self.access_token)
            
            with open (file_to,'rb')as f:
                kk.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))

def main ():
    access_token = "sl.A2WrXqGFAjCCCmh8wgn-10M7zKk3c6I23ntusrEapn5bEqE5UnbQDVw0Y4D20yebkUnVDoyqKe5k3zlNtGkARudR0mR1OgUjUwcHWeY34Oa2eoZuwcd-z_n1vl4MqIPTin24lw4"
    uploadfiles = Uploadfiles(access_token)

    file_from = "kavish.txt"
    file_to = "kavish.txt"

    uploadfiles.upload_file(file_from,file_to)
    print("File has been uploaded")

main()