# EMA Hourly Continuation — ENA/USDT P21_200

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.8110 |
| sortino_ratio | -0.5005 |
| max_drawdown | 0.4907 |
| cagr | -0.2088 |
| net_avg_win | 65.2599 |
| net_avg_loss | -83.1011 |
| avg_hold_time_bars | 35.5262 |
| exposure | 0.6169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
