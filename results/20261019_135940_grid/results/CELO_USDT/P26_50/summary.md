# EMA Hourly Continuation — CELO/USDT P26_50

**Symbol:** CELO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.4516 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8190 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -7.1031 |
| sortino_ratio | -3.0654 |
| max_drawdown | 0.9763 |
| cagr | -0.7721 |
| net_avg_win | 19.3229 |
| net_avg_loss | -34.5603 |
| avg_hold_time_bars | 4.2879 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
