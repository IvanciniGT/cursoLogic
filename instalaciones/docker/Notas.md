docker run -d 
      -p 9001:7001 
      -p 9002:9002 \
      -v $PWD:/u01/oracle/properties  \
      -e DOMAIN_NAME=base_domain \
      store/oracle/weblogic:12.2.1.4
      