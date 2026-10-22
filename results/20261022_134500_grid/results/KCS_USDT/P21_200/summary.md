# EMA Hourly Continuation — KCS/USDT P21_200

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.4377 |
| net_win_rate | 0.3945 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -6.1574 |
| sortino_ratio | -1.7492 |
| max_drawdown | 0.8916 |
| cagr | -0.5872 |
| net_avg_win | 43.6525 |
| net_avg_loss | -64.9871 |
| avg_hold_time_bars | 33.5558 |
| exposure | 0.6147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
