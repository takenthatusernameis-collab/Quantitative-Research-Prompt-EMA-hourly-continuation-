# EMA Hourly Continuation — CERE/USDT P34_100

**Symbol:** CERE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.4637 |
| net_win_rate | 0.3421 |
| gross_profit_factor | 0.8322 |
| gross_win_rate | 0.3697 |
| sharpe_ratio | -9.9846 |
| sortino_ratio | -3.8304 |
| max_drawdown | 0.9941 |
| cagr | -0.8647 |
| net_avg_win | 34.6414 |
| net_avg_loss | -38.8369 |
| avg_hold_time_bars | 9.3890 |
| exposure | 0.3094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
