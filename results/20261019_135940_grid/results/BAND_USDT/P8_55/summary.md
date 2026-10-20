# EMA Hourly Continuation — BAND/USDT P8_55

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 1.0079 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -4.7288 |
| sortino_ratio | -1.9744 |
| max_drawdown | 0.9102 |
| cagr | -0.6134 |
| net_avg_win | 37.9703 |
| net_avg_loss | -53.8108 |
| avg_hold_time_bars | 12.6223 |
| exposure | 0.5066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
