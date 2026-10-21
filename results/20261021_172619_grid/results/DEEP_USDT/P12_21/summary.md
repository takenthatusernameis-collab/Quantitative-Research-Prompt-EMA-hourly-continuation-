# EMA Hourly Continuation — DEEP/USDT P12_21

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 1.1311 |
| net_win_rate | 0.6063 |
| gross_profit_factor | 1.5101 |
| gross_win_rate | 0.6063 |
| sharpe_ratio | 0.8009 |
| sortino_ratio | 0.2102 |
| max_drawdown | 0.1218 |
| cagr | 0.0870 |
| net_avg_win | 102.6188 |
| net_avg_loss | -139.7168 |
| avg_hold_time_bars | 4.6102 |
| exposure | 0.0663 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
