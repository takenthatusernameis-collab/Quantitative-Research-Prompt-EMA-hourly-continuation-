# EMA Hourly Continuation — RENDER/USDT P21_144

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7570 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -2.0983 |
| sortino_ratio | -0.6552 |
| max_drawdown | 0.5488 |
| cagr | -0.2662 |
| net_avg_win | 72.7438 |
| net_avg_loss | -95.6380 |
| avg_hold_time_bars | 23.6754 |
| exposure | 0.5236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
