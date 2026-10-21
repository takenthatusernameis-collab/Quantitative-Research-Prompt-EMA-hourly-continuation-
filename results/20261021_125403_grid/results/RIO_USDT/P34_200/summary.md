# EMA Hourly Continuation — RIO/USDT P34_200

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7106 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7938 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -1.9734 |
| sortino_ratio | -0.4873 |
| max_drawdown | 0.4600 |
| cagr | -0.2023 |
| net_avg_win | 79.3535 |
| net_avg_loss | -86.8601 |
| avg_hold_time_bars | 34.2467 |
| exposure | 0.4780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
