"""An example to check Persistent Volume Claim"""

import os

def test_SC(kube):

    f = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "configs", "sc.yaml"
    )

    d = kube.load_storage_class(f)

    kube.create(d)
    d.wait_until_ready(timeout=200)
    d.refresh()
    kube.delete(d)
    d.wait_until_deleted(timeout=20)
