# EMA Hourly Continuation — SQD/USDT P8_20

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -2.3493 |
| sortino_ratio | -0.7650 |
| max_drawdown | 0.6011 |
| cagr | -0.2962 |
| net_avg_win | 64.3179 |
| net_avg_loss | -80.7581 |
| avg_hold_time_bars | 5.1369 |
| exposure | 0.1217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
