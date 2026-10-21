# EMA Hourly Continuation — INJ/USDT P100_200

**Symbol:** INJ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7378 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9087 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -1.4925 |
| sortino_ratio | -0.3412 |
| max_drawdown | 0.3474 |
| cagr | -0.1455 |
| net_avg_win | 74.6016 |
| net_avg_loss | -92.8194 |
| avg_hold_time_bars | 13.1362 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
