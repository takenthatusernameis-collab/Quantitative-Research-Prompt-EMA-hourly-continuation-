# EMA Hourly Continuation — BTT/USDT P20_200

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.4405 |
| net_win_rate | 0.4281 |
| gross_profit_factor | 0.7776 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -4.2948 |
| sortino_ratio | -1.0357 |
| max_drawdown | 0.7435 |
| cagr | -0.4097 |
| net_avg_win | 45.1431 |
| net_avg_loss | -76.7052 |
| avg_hold_time_bars | 50.7458 |
| exposure | 0.6897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
