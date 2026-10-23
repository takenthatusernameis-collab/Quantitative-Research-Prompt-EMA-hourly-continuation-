# EMA Hourly Continuation — ONE/USDT P26_200

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7585 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9865 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.7095 |
| sortino_ratio | -0.4491 |
| max_drawdown | 0.4447 |
| cagr | -0.1905 |
| net_avg_win | 76.1124 |
| net_avg_loss | -98.0333 |
| avg_hold_time_bars | 40.0727 |
| exposure | 0.6266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
