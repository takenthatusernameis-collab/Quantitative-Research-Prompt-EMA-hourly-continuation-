# EMA Hourly Continuation — XTZ/USDT P8_200

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.8590 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0588 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -0.6621 |
| sortino_ratio | -0.1462 |
| max_drawdown | 0.2131 |
| cagr | -0.0667 |
| net_avg_win | 79.5275 |
| net_avg_loss | -99.0771 |
| avg_hold_time_bars | 78.7415 |
| exposure | 0.8447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
