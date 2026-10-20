# EMA Hourly Continuation — CGPT/USDT P26_144

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7225 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.0007 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -2.3766 |
| sortino_ratio | -0.7153 |
| max_drawdown | 0.5767 |
| cagr | -0.2873 |
| net_avg_win | 67.4932 |
| net_avg_loss | -89.3678 |
| avg_hold_time_bars | 22.4801 |
| exposure | 0.4619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
