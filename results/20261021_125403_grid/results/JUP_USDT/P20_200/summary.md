# EMA Hourly Continuation — JUP/USDT P20_200

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7623 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8811 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -1.6269 |
| sortino_ratio | -0.4097 |
| max_drawdown | 0.4550 |
| cagr | -0.1729 |
| net_avg_win | 82.7430 |
| net_avg_loss | -94.4098 |
| avg_hold_time_bars | 41.0665 |
| exposure | 0.5899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
