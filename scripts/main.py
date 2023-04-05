from wf import run_dada2
from wf.types import Sample, TaxonomyReference, SpeciesAssignmentReference
from latch.types import LatchFile


run_dada2(
    samples=[
        Sample(
            read1=LatchFile("s3://latch-public/test-data/4318/F3D0_S188_L001_1.fastq"),
            read2=LatchFile("s3://latch-public/test-data/4318/F3D0_S188_L001_2.fastq"),
        ),
        Sample(
            read1=LatchFile("s3://latch-public/test-data/4318/F3D8_S196_L001_1.fastq"),
            read2=LatchFile("s3://latch-public/test-data/4318/F3D8_S196_L001_2.fastq"),
        ),
        Sample(
            read1=LatchFile(
                "s3://latch-public/test-data/4318/F3D149_S215_L001_1.fastq"
            ),
            read2=LatchFile(
                "s3://latch-public/test-data/4318/F3D149_S215_L001_2.fastq"
            ),
        ),
    ],
    taxonomy_reference=TaxonomyReference.SILVA,
    species_assignment=SpeciesAssignmentReference.SILVA,
    taxonomy_ref_fasta=None,
    species_assignment_fasta=None,
    minLen=50,
    maxN=0,
    minQ=0,
    maxEE=2,
    truncQ=2,
    trimLeft=0,
    trimRight=0,
)

run_dada2(
    samples=[
        Sample(
            read1=LatchFile(
                "s3://latch-public/test-data/4318/PRJNA377530_trimmed/SRR5314314_trim_1.fastq.gz"
            ),
            read2=LatchFile(
                "s3://latch-public/test-data/4318/PRJNA377530_trimmed/SRR5314314_trim_2.fastq.gz"
            ),
        ),
        Sample(
            read1=LatchFile(
                "s3://latch-public/test-data/4318/PRJNA377530_trimmed/SRR5314336_trim_1.fastq.gz"
            ),
            read2=LatchFile(
                "s3://latch-public/test-data/4318/PRJNA377530_trimmed/SRR5314336_trim_2.fastq.gz"
            ),
        ),
        Sample(
            read1=LatchFile(
                "s3://latch-public/test-data/4318/PRJNA377530_trimmed/SRR5838532_trim_1.fastq.gz"
            ),
            read2=LatchFile(
                "s3://latch-public/test-data/4318/PRJNA377530_trimmed/SRR5838532_trim_2.fastq.gz"
            ),
        ),
    ],
    taxonomy_ref_fasta=LatchFile(
        "s3://latch-public/test-data/4318/sh_general_release_dynamic_29.11.2022.fasta"
    ),
    taxonomy_reference=TaxonomyReference.SILVA,
    species_assignment_fasta=None,
    species_assignment=None,
    minLen=50,
    maxN=0,
    minQ=0,
    maxEE=2,
    truncQ=2,
    trimLeft=0,
    trimRight=0,
)
