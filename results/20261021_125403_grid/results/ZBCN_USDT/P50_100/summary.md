# EMA Hourly Continuation — ZBCN/USDT P50_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8356 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.1480 |
| sortino_ratio | -0.5633 |
| max_drawdown | 0.4992 |
| cagr | -0.2282 |
| net_avg_win | 66.7443 |
| net_avg_loss | -82.4191 |
| avg_hold_time_bars | 7.2232 |
| exposure | 0.1123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
