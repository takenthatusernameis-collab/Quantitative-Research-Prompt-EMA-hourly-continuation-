# EMA Hourly Continuation — ORDI/USDT P100_144

**Symbol:** ORDI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.6875 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -1.7384 |
| sortino_ratio | -0.3986 |
| max_drawdown | 0.3762 |
| cagr | -0.1674 |
| net_avg_win | 65.4359 |
| net_avg_loss | -88.7343 |
| avg_hold_time_bars | 5.6070 |
| exposure | 0.0655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
