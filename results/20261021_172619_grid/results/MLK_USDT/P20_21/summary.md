# EMA Hourly Continuation — MLK/USDT P20_21

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.2888 |
| net_win_rate | 0.3059 |
| gross_profit_factor | 0.4877 |
| gross_win_rate | 0.3105 |
| sharpe_ratio | -5.4909 |
| sortino_ratio | -1.1565 |
| max_drawdown | 0.7649 |
| cagr | -0.4294 |
| net_avg_win | 45.8859 |
| net_avg_loss | -70.0392 |
| avg_hold_time_bars | 5.5616 |
| exposure | 0.0551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
