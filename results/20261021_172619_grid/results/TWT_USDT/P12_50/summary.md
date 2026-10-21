# EMA Hourly Continuation — TWT/USDT P12_50

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0523 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -2.2392 |
| sortino_ratio | -0.8469 |
| max_drawdown | 0.6523 |
| cagr | -0.3212 |
| net_avg_win | 51.3497 |
| net_avg_loss | -73.7295 |
| avg_hold_time_bars | 10.5304 |
| exposure | 0.3303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
