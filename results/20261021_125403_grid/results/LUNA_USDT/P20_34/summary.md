# EMA Hourly Continuation — LUNA/USDT P20_34

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8844 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -2.5474 |
| sortino_ratio | -0.5960 |
| max_drawdown | 0.5009 |
| cagr | -0.2391 |
| net_avg_win | 69.5625 |
| net_avg_loss | -93.2557 |
| avg_hold_time_bars | 5.4813 |
| exposure | 0.0668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
