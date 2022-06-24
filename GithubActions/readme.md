# Github Actions


Secure checkout
```
    steps:
      - name: "Checkout ${{ github.ref }} ( ${{ github.sha }} )"
        uses: actions/checkout@v3
        with:
          persist-credentials: false
```
