"""An example to check Persistent Volume Claim"""

import os


def test_deployment(kube):

    f = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "configs", "pvc.yaml"
    )

    d = kube.load_persistentvolumeclaim(f)

    kube.create(d)

    d.wait_until_ready(timeout=200)
    d.refresh()
    print("PVC Created")
    kube.delete(d)
    d.wait_until_deleted(timeout=20)
