# EMA Hourly Continuation — ORDI/USDT P21_200

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6922 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -2.6262 |
| sortino_ratio | -0.7693 |
| max_drawdown | 0.6177 |
| cagr | -0.3044 |
| net_avg_win | 66.5873 |
| net_avg_loss | -83.7567 |
| avg_hold_time_bars | 29.1682 |
| exposure | 0.5754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
