# EMA Hourly Continuation — INJ/USDT P12_34

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0136 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.7903 |
| sortino_ratio | -0.6138 |
| max_drawdown | 0.5162 |
| cagr | -0.2463 |
| net_avg_win | 68.2412 |
| net_avg_loss | -86.8625 |
| avg_hold_time_bars | 7.3380 |
| exposure | 0.1905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
