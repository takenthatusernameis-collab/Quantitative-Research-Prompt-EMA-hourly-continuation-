# EMA Hourly Continuation — SQD/USDT P21_89

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.8938 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 1.0613 |
| gross_win_rate | 0.5157 |
| sharpe_ratio | -0.7954 |
| sortino_ratio | -0.2621 |
| max_drawdown | 0.3691 |
| cagr | -0.1181 |
| net_avg_win | 84.5059 |
| net_avg_loss | -100.6912 |
| avg_hold_time_bars | 13.8071 |
| exposure | 0.3297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
