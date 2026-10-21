# EMA Hourly Continuation — ENA/USDT P89_100

**Symbol:** ENA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 62 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9357 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -0.7853 |
| sortino_ratio | -0.0884 |
| max_drawdown | 0.1539 |
| cagr | -0.0397 |
| net_avg_win | 85.4541 |
| net_avg_loss | -110.3163 |
| avg_hold_time_bars | 4.1129 |
| exposure | 0.0116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
