# EMA Hourly Continuation — CVX/USDT P20_200

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.8902 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0185 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -0.5468 |
| sortino_ratio | -0.1226 |
| max_drawdown | 0.1867 |
| cagr | -0.0574 |
| net_avg_win | 90.2092 |
| net_avg_loss | -103.8450 |
| avg_hold_time_bars | 62.2571 |
| exposure | 0.6933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
