# EMA Hourly Continuation — ORCA/USDT P34_100

**Symbol:** ORCA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7559 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9707 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.8355 |
| sortino_ratio | -0.5470 |
| max_drawdown | 0.5095 |
| cagr | -0.2230 |
| net_avg_win | 67.2795 |
| net_avg_loss | -87.7893 |
| avg_hold_time_bars | 13.7310 |
| exposure | 0.2715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
