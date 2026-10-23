# EMA Hourly Continuation — BRETT/USDT P26_55

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 879 |
| net_profit_factor | 0.5340 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.8231 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -6.7284 |
| sortino_ratio | -2.8814 |
| max_drawdown | 0.9648 |
| cagr | -0.7541 |
| net_avg_win | 29.1457 |
| net_avg_loss | -41.3750 |
| avg_hold_time_bars | 4.4096 |
| exposure | 0.1865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
