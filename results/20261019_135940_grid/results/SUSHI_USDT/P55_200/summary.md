# EMA Hourly Continuation — SUSHI/USDT P55_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9509 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -2.7737 |
| sortino_ratio | -0.8091 |
| max_drawdown | 0.6341 |
| cagr | -0.3148 |
| net_avg_win | 53.3799 |
| net_avg_loss | -76.4999 |
| avg_hold_time_bars | 19.0682 |
| exposure | 0.3667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
