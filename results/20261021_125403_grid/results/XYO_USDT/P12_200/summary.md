# EMA Hourly Continuation — XYO/USDT P12_200

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6470 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8330 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -2.7006 |
| sortino_ratio | -0.7749 |
| max_drawdown | 0.6301 |
| cagr | -0.3007 |
| net_avg_win | 57.6473 |
| net_avg_loss | -75.8502 |
| avg_hold_time_bars | 36.2068 |
| exposure | 0.6734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
