# EMA Hourly Continuation — NFT/USDT P8_21

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2251 |
| net_profit_factor | 0.1101 |
| net_win_rate | 0.1795 |
| gross_profit_factor | 0.4580 |
| gross_win_rate | 0.2510 |
| sharpe_ratio | -31.2214 |
| sortino_ratio | -23.7803 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 3.0620 |
| net_avg_loss | -6.0840 |
| avg_hold_time_bars | 2.5069 |
| exposure | 0.2565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
