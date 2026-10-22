# EMA Hourly Continuation — MTL/USDT P12_21

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5155 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8988 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -5.5208 |
| sortino_ratio | -1.9292 |
| max_drawdown | 0.9020 |
| cagr | -0.5972 |
| net_avg_win | 34.6610 |
| net_avg_loss | -57.8126 |
| avg_hold_time_bars | 5.1139 |
| exposure | 0.1382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
