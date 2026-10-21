# EMA Hourly Continuation — HTX/USDT P50_200

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.4718 |
| net_win_rate | 0.3938 |
| gross_profit_factor | 0.7204 |
| gross_win_rate | 0.3938 |
| sharpe_ratio | -4.5970 |
| sortino_ratio | -1.1219 |
| max_drawdown | 0.7425 |
| cagr | -0.4114 |
| net_avg_win | 57.2759 |
| net_avg_loss | -78.8731 |
| avg_hold_time_bars | 31.2158 |
| exposure | 0.4125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
