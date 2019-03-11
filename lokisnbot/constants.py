
PROOF_AGE_WARNING = 3600 + 300  # 1 hour plus 5 minutes of grace time (uptime proofs can take slightly more than an hour)
PROOF_AGE_REPEAT = 600  # How often to repeat the alert
STAKE_BLOCKS = 720*30 + 20  # Length of a stake (pre-3.0.0)
TESTNET_STAKE_BLOCKS = 720*2 + 20  # Length of a stake (pre-3.0.0)
INFINITE_FROM = 235024  # Tentative -- update when finalized in lokid
TESTNET_INFINITE_FROM = 1  # Testnet is always infinite
AVERAGE_BLOCK_SECONDS = 120  # Target block time
COIN = 1000000000  # Number of atomic units in 1 coin

