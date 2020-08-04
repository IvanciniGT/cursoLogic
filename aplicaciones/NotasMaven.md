# Comandos MAVEN
## Crear un proyecto nuevo JAVA
Con maven los proyectos desde una plantilla: ARQUETIPO
    mvn archetype:generate \
        -DarchetypeArtifactId=maven-archetype-webapp \
        -DartifactId=miwebapp \
        -DgroupId=es.manpower.curso \
        -DinteractiveMode=false