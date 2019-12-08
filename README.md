# Interactive Etch Demo and Prototyping Tool

Easily spin-up your own browser-based app locally to deploy and interact with your Etch contract. This allow for rapid prototyping and QA testing through a UI/UX. This is loosely based off of [Ethereum Remix](https://remix.ethereum.org/) IDE.

### Steps for Launching the App

1) Spin-up a local Fetch ledger. See Fetch's Getting Started doc [here](https://docs.fetch.ai/getting-started/quickstart/).
2) Install the following packages:
```
pip install Flask
pip install fetchai-ledger-api
```
3) Run `git clone` this repo to your local directory
4) Run `cd etch-demos/app/`
5) Run `python start.py` to start the app on the localhost. You should see the following message on your console:
```
 * Serving Flask app "start" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```
6) Copy-paste this link `http://127.0.0.1:5000/` into the browser of your choice.
7) Click on `Info` for more detail about how to use this app.


### Sample Etch Contracts

This repo comes with three sample Etch contracts that you can use to experiment with the app. More samples will be added.

1) **Hello World** See contract at [hello.etch](https://github.com/fetchai/etch-demos/blob/master/demos/hello-world/hello.etch).
2) **Pet Shop** dApp from the Truffle [tutorial](https://www.trufflesuite.com/tutorials/pet-shop). See contract at [adoption.etch](https://github.com/fetchai/etch-demos/blob/master/demos/pet-shop/adoption.etch).
3) **Simple Open Auction** dApp from the Ethereum Vyper [tutorial](https://vyper.readthedocs.io/en/v0.1.0-beta.13/vyper-by-example.html#simple-open-auction). See contract at [auction](https://github.com/fetchai/etch-demos/blob/master/demos/simple-open-auction/auction.etch).

It may be migrated to etch-examples: https://github.com/fetchai/etch-examples



