nextflow.enable.dsl=2

params.clinvar = ''
params.testregion = ''

include {PARSE_CLINVAR}     from './process/parse_clinvar'
include {PARSE_TESTREGION}  from './process/parse_testregion'
include {COUNTING_MATRIX}   from './process/counting_matrix'

workflow {
    PARSE_CLINVAR(params.clinvar)
    PARSE_TESTREGION(PARSE_CLINVAR.out.parsed_clinvar, params.testregion)
    COUNTING_MATRIX(PARSE_CLINVAR.out.parsed_clinvar, PARSE_TESTREGION.out.parsed_testregion)
}