# EMA Hourly Continuation — NFT/USDT P89_144

**Symbol:** NFT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.2607 |
| net_win_rate | 0.2897 |
| gross_profit_factor | 0.5090 |
| gross_win_rate | 0.2976 |
| sharpe_ratio | -6.7119 |
| sortino_ratio | -1.5702 |
| max_drawdown | 0.8465 |
| cagr | -0.5230 |
| net_avg_win | 40.7695 |
| net_avg_loss | -63.7847 |
| avg_hold_time_bars | 11.2579 |
| exposure | 0.1290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
