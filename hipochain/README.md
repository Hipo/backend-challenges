# Hipochain
## Objectives
* send transactions.
* parse transactions.
* implement ledgering.

## Assumptions
* No consensus.
* No peer to peer gossip.
* No authentication.
* There exists a Redis client which is used for broadcasting the transactions.
* Redis client is accessable by everyone under the local network.
* Transactions are stored in a Redis List which is accessed by the key `hiponet`.
* New transactions are appended to the end of the Redis list.
* Some of the submitted transactions might be invalid.
* There is only one asset whose `id` is 0.
* Every account, **except** HIPO, has 0 asset balance at the start.
* HIPO creates the genesis transaction, which distributes the assets.
* HIPO is trustable. No need to perform validations for their transactions.

## Protocol
* Transaction must be a JSON Array of objects.
* Transaction must contain the fields below:
  * `amount`
  * `asset_id`
  * `first_valid`
  * `receiver`
  * `sender`
  * `type`
* Transaction `sender`, `receiver` and `type` should be strings.
* Transaction `amount`, `asset_id` and `first_valid` should be integers.
* Each valid transaction group increments an internal variable `round` which starts from 0 before the first transactions.
* `first_valid` must be smaller or equal to the current round at the time of transaction validation.
* Reject (ignore) transactions that cause overspend (negative amounts). Remember, in HIPO we trust.
* Transactions after `round` 2 must not have HIPO as `sender`.
* If a group contains more than 1 transaction, reject ALL transactions in the group if ANY transaction fails for any reason.
* Transaction `amount` must be non-negative.
* Transaction `type` must be `transfer`.
* `asset_id` must be 0.

## Steps
1. Connect to redis and print contents of `hiponet` list.
2. Continuously check list and print new messages `(while True:…)`.
3. Connect to redis and append to the `hiponet` list. Use `rpush`.
4. Filter messages and discard anything that is not a valid JSON array of objects.
5. Manually/mentally parse the valid looking transactions to see the flow of funds to accounts.
6. Send a transaction of the same format as the existing transactions.
7. Implement ledgering (accounting logic). Keep running balances of accounts. Reject (ignore) transactions that cause overspend (negative amounts)
8. Stop and compare balances after round 42.

## External Links
* [Redis List Commands](https://redis.io/commands/?group=list)
* [2022 Backend Day Slack Thread](https://hipo.slack.com/archives/C0G5PTL8Z/p1650618219636349)
