# EMA Hourly Continuation — CHR/USDT P50_55

**Symbol:** CHR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 154 |
| net_profit_factor | 0.6355 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.8753 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -1.7238 |
| sortino_ratio | -0.3049 |
| max_drawdown | 0.3126 |
| cagr | -0.1297 |
| net_avg_win | 71.5935 |
| net_avg_loss | -98.9225 |
| avg_hold_time_bars | 8.8312 |
| exposure | 0.0615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
