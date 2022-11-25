process PARSE_CLINVAR {
    publishDir "results/", mode: "copy"

    input:
        val clinvar

    output:
        path '*_db.csv', emit: parsed_clinvar

    script:
        """
        parse_clinvar.py $clinvar
        """
}
