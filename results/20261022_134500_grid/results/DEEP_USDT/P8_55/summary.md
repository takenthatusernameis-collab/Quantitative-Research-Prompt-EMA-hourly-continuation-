# EMA Hourly Continuation — DEEP/USDT P8_55

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.7178 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -3.8198 |
| sortino_ratio | -1.6797 |
| max_drawdown | 0.8125 |
| cagr | -0.5510 |
| net_avg_win | 54.1857 |
| net_avg_loss | -70.0833 |
| avg_hold_time_bars | 11.0576 |
| exposure | 0.4890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
