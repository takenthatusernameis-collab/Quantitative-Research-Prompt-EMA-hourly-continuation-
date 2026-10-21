# EMA Hourly Continuation — NMR/USDT P89_200

**Symbol:** NMR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7459 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 0.9885 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -1.5289 |
| sortino_ratio | -0.3825 |
| max_drawdown | 0.3893 |
| cagr | -0.1617 |
| net_avg_win | 68.6638 |
| net_avg_loss | -92.6577 |
| avg_hold_time_bars | 13.6164 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
