# EMA Hourly Continuation — BLZ/USDT P8_12

**Symbol:** BLZ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1786 |
| net_profit_factor | 0.2956 |
| net_win_rate | 0.3393 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.3942 |
| sharpe_ratio | -17.9841 |
| sortino_ratio | -10.9176 |
| max_drawdown | 1.0000 |
| cagr | -0.9969 |
| net_avg_win | 6.9257 |
| net_avg_loss | -12.0313 |
| avg_hold_time_bars | 2.5207 |
| exposure | 0.2037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
