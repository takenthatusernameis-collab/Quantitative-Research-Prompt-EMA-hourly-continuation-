# EMA Hourly Continuation — LSK/USDT P8_12

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.6359 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0602 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -3.4429 |
| sortino_ratio | -1.1177 |
| max_drawdown | 0.7398 |
| cagr | -0.4029 |
| net_avg_win | 49.9177 |
| net_avg_loss | -78.5053 |
| avg_hold_time_bars | 5.7047 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
