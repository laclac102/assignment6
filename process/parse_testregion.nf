process PARSE_TESTREGION {
    publishDir "results/", mode: "copy"

    input:
        path parsed_clinvar
        val region

    output:
        path 'parsed_testregion.csv', emit: parsed_testregion

    script:
        """
        parse_testregion.py $region $parsed_clinvar
        """
}
