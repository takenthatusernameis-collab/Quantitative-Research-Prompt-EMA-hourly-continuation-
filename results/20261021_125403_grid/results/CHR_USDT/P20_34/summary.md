# EMA Hourly Continuation — CHR/USDT P20_34

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6279 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -3.2463 |
| sortino_ratio | -0.9620 |
| max_drawdown | 0.6725 |
| cagr | -0.3566 |
| net_avg_win | 57.2196 |
| net_avg_loss | -76.7756 |
| avg_hold_time_bars | 5.8152 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
