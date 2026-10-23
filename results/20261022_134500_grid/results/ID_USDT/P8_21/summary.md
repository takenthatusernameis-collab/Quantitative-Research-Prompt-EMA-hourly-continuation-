# EMA Hourly Continuation — ID/USDT P8_21

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1436 |
| net_profit_factor | 0.4177 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.9516 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -10.4631 |
| sortino_ratio | -5.5969 |
| max_drawdown | 0.9992 |
| cagr | -0.9373 |
| net_avg_win | 11.7280 |
| net_avg_loss | -20.7958 |
| avg_hold_time_bars | 3.9178 |
| exposure | 0.2546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
