# EMA Hourly Continuation — POPCAT/USDT P21_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7117 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8396 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -2.2611 |
| sortino_ratio | -0.6913 |
| max_drawdown | 0.5086 |
| cagr | -0.2730 |
| net_avg_win | 66.8192 |
| net_avg_loss | -79.9731 |
| avg_hold_time_bars | 19.2150 |
| exposure | 0.4060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
