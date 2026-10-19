# EMA Hourly Continuation — IMX/USDT P12_34

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.4945 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -7.8066 |
| sortino_ratio | -3.8066 |
| max_drawdown | 0.9919 |
| cagr | -0.8453 |
| net_avg_win | 17.8533 |
| net_avg_loss | -29.1728 |
| avg_hold_time_bars | 4.5588 |
| exposure | 0.2506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
