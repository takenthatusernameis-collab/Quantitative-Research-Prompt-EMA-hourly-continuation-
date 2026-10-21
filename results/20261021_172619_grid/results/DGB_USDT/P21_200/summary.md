# EMA Hourly Continuation — DGB/USDT P21_200

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7655 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -1.7380 |
| sortino_ratio | -0.4827 |
| max_drawdown | 0.4877 |
| cagr | -0.2005 |
| net_avg_win | 77.0954 |
| net_avg_loss | -92.1135 |
| avg_hold_time_bars | 33.8058 |
| exposure | 0.5855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
