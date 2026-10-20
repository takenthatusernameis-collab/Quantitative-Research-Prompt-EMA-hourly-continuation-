# EMA Hourly Continuation — FLUX/USDT P20_100

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6521 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 1.0066 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -3.5170 |
| sortino_ratio | -1.3031 |
| max_drawdown | 0.8049 |
| cagr | -0.4649 |
| net_avg_win | 43.2754 |
| net_avg_loss | -65.0395 |
| avg_hold_time_bars | 13.5830 |
| exposure | 0.4279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
