import pytest 

@pytest.fixture(scope='package',autouse=True)
def st_emptyEnv():
    print(f'\n==== setup：：emptyEnv')
    yield
    
    print(f'\n==== teardown：：emptyEnv')