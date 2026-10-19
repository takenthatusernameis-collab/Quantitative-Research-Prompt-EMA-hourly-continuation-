# EMA Hourly Continuation — SKY/USDT P89_100

**Symbol:** SKY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.3114 |
| net_win_rate | 0.4081 |
| gross_profit_factor | 0.9161 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -9.1823 |
| sortino_ratio | -3.2571 |
| max_drawdown | 0.9728 |
| cagr | -0.8255 |
| net_avg_win | 21.7642 |
| net_avg_loss | -48.1778 |
| avg_hold_time_bars | 2.2202 |
| exposure | 0.0613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
