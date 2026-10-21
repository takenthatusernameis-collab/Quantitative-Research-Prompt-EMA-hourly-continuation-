# EMA Hourly Continuation — IO/USDT P26_55

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7938 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9841 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.4107 |
| sortino_ratio | -0.3989 |
| max_drawdown | 0.3809 |
| cagr | -0.1680 |
| net_avg_win | 74.4065 |
| net_avg_loss | -92.7191 |
| avg_hold_time_bars | 7.3087 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
