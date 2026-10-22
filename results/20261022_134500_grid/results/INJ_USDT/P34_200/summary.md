# EMA Hourly Continuation — INJ/USDT P34_200

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6266 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -2.7648 |
| sortino_ratio | -0.7465 |
| max_drawdown | 0.6109 |
| cagr | -0.3006 |
| net_avg_win | 57.8094 |
| net_avg_loss | -78.9497 |
| avg_hold_time_bars | 28.8499 |
| exposure | 0.4891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
