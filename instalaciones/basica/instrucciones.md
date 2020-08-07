# Instrucciones para Instalar WEBLOGIC
## Prerequisitos
### Swap
Web logic requiere al menos 500Mbs de Swap
    sudo swapoff -a
    sudo dd if=/dev/zero of=/var/swapfile bs=100M count=6
    sudo chmod 600 /var/swapfile
    sudo mkswap /var/swapfile
    sudo swapon /var/swapfile
    free
### Oracle JDK
sudo tar -C /usr/lib/jvm -xvzf ~/environment/jdk-8u261-linux-x64.tar.gz

echo PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/jvm/jdk1.8.0_261/bin:/usr/lib/jvm/jdk1.8.0_261/db/bin:/usr/lib/jvm/jdk1.8.0_261/jre/bin\" | sudo tee -a /etc/environment
echo JAVA_HOME=\"/usr/lib/jvm/jdk1.8.0_261\" | sudo tee -a /etc/environment
source /etc/environment

sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_261/bin/java" 0
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_261/bin/javac" 0
sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_261/bin/java
sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_261/bin/javac

rm ~/environment/jdk-8u261-linux-x64.tar.gz

## Instalacion
### Descomprimir el ZIP de instalación
unzip fmw_12.2.1.4.0_wls_quick_Disk1_1of1.zip 

### Ejecución del programa de instalación
java -jar fmw_12.2.1.4.0_wls_quick.jar -silent

### Configuración:
echo MW_HOME=/home/ubuntu/environment/wls12214 | sudo tee -a /etc/environment
export MW_HOME=/home/ubuntu/environment/wls12214 

cd /home/ubuntu/environment/wls12214/oracle_common/common/bin
./commEnv.sh      # Establece varias de entorno para poder operar sobre weblogic
./wlst.sh         # CLI
DE WEBLOGIC


## Creación del dominio y servidor
readTemplate('/home/ubuntu/environment/wls12214/wlserver/common/templates/wls/wls.jar')
cd('Servers/AdminServer')
set('ListenAddress','172.31.12.96')
set('ListenPort', 7001)
create('AdminServer','SSL')
cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', 7002)
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('passw0rd')
setOption('OverwriteDomain', 'true')
writeDomain('/home/ubuntu/environment/wls12214/user_projects/domains/MI_DOMINIO')
closeTemplate()
exit()




readDomain('/home/ubuntu/environment/wls12214/user_projects/domains/MI_DOMINIO')
cd('Servers/AdminServer')
set('ListenAddress','172.31.12.96')
updateDomain()
exit()