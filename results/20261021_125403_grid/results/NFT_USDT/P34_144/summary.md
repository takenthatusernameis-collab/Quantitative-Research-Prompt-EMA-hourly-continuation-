# EMA Hourly Continuation — NFT/USDT P34_144

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.4090 |
| net_win_rate | 0.3485 |
| gross_profit_factor | 0.6652 |
| gross_win_rate | 0.3510 |
| sharpe_ratio | -6.5641 |
| sortino_ratio | -1.8818 |
| max_drawdown | 0.8964 |
| cagr | -0.5862 |
| net_avg_win | 44.6733 |
| net_avg_loss | -58.4279 |
| avg_hold_time_bars | 21.8838 |
| exposure | 0.3939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
