# EMA Hourly Continuation — CHR/USDT P20_100

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6250 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8909 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -4.0900 |
| sortino_ratio | -1.4845 |
| max_drawdown | 0.8404 |
| cagr | -0.5042 |
| net_avg_win | 45.4925 |
| net_avg_loss | -61.2921 |
| avg_hold_time_bars | 14.4316 |
| exposure | 0.4343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
