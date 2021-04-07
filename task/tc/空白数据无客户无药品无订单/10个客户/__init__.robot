*** Settings ***
Library  pylib.APImgr

Suite Setup     run keywords    add_customers   武汉市桥西医院1     13345679931     武汉市桥西医院北路1
                ...      AND    add_customers   武汉市桥西医院2     13345679932     武汉市桥西医院北路2
                ...      AND    add_customers   武汉市桥西医院3     13345679933     武汉市桥西医院北路3
                ...      AND    add_customers   武汉市桥西医院4     13345679934     武汉市桥西医院北路4
                ...      AND    add_customers   武汉市桥西医院5     13345679935     武汉市桥西医院北路5
                ...      AND    add_customers   武汉市桥西医院6     13345679936     武汉市桥西医院北路6
                ...      AND    add_customers   武汉市桥西医院7     13345679937     武汉市桥西医院北路7
                ...      AND    add_customers   武汉市桥西医院8     13345679938     武汉市桥西医院北路8
                ...      AND    add_customers   武汉市桥西医院9     13345679939     武汉市桥西医院北路9
                ...      AND    add_customers   武汉市桥西医院10    13345679940     武汉市桥西医院北路10
Suite Teardown  delete_all_customers