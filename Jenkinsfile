node {
      stage('build') {
         sh '''
           cd /var/lib/jenkins/MyProject/virtual-machines-python-manage 
           pip install -r requirements.txt
           python /var/lib/jenkins/MyProject/virtual-machines-python-manage/example.py
         '''
   }
} 
