# EMA Hourly Continuation — PUFFER/USDT P34_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8590 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0182 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -0.8660 |
| sortino_ratio | -0.2460 |
| max_drawdown | 0.2163 |
| cagr | -0.1101 |
| net_avg_win | 79.8650 |
| net_avg_loss | -95.9730 |
| avg_hold_time_bars | 20.3873 |
| exposure | 0.3634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
