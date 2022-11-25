### How this pipe could be deployed

```
nextflow run assignment6.nf --clinvar /path/to/the/data/from/clinvar --testregion path/to/grch37.testregion.bed --with-docker assignment6
```
while assignment6 container could be built with the following command in the Dockerfile location:

```
docker build -t assignment6 .
```