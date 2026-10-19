# EMA Hourly Continuation — CHZ/USDT P8_21

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1715 |
| net_profit_factor | 0.4098 |
| net_win_rate | 0.4268 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -12.5877 |
| sortino_ratio | -7.3498 |
| max_drawdown | 0.9999 |
| cagr | -0.9766 |
| net_avg_win | 9.4851 |
| net_avg_loss | -17.2353 |
| avg_hold_time_bars | 3.0717 |
| exposure | 0.2395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
