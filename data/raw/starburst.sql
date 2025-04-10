SELECT TOP 5000
    s.specObjID AS objID,
    s.plate,
    s.mjd,
    s.fiberID,
    s.class,
    s.subClass,
    s.z AS redshift,
    s.zErr AS redshiftError,
    s.velDisp AS velocityDispersion,
    s.velDispErr AS velocityDispersionError,
    'https://data.sdss.org/sas/dr18/spectro/sdss/redux/v5_13_2/spectra/lite/' +
    CASE
        WHEN LEN(CAST(s.plate AS VARCHAR)) = 4 THEN
            RIGHT('0000' + CAST(s.plate AS VARCHAR), 4) + '/' + 
            'spec-' + RIGHT('0000' + CAST(s.plate AS VARCHAR), 4) + '-' + 
            CAST(s.mjd AS VARCHAR) + '-' + 
            RIGHT('0000' + CAST(s.fiberID AS VARCHAR), 4) + '.fits'
        WHEN LEN(CAST(s.plate AS VARCHAR)) = 5 THEN
            RIGHT('00000' + CAST(s.plate AS VARCHAR), 5) + '/' + 
            'spec-' + RIGHT('00000' + CAST(s.plate AS VARCHAR), 5) + '-' + 
            CAST(s.mjd AS VARCHAR) + '-' + 
            RIGHT('0000' + CAST(s.fiberID AS VARCHAR), 4) + '.fits'
    END
FROM
    SpecObj AS s
WHERE
    s.class = 'GALAXY'
    AND (s.subClass LIKE '%starburst%')
    AND s.zWarning = 0
