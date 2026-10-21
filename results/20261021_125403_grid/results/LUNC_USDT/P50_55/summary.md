# EMA Hourly Continuation — LUNC/USDT P50_55

**Symbol:** LUNC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 91 |
| net_profit_factor | 0.6225 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -1.3596 |
| sortino_ratio | -0.1856 |
| max_drawdown | 0.1999 |
| cagr | -0.0815 |
| net_avg_win | 73.7758 |
| net_avg_loss | -106.1626 |
| avg_hold_time_bars | 5.5604 |
| exposure | 0.0230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
