# EMA Hourly Continuation — TNSR/USDT P8_144

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.8284 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -1.3608 |
| sortino_ratio | -0.3918 |
| max_drawdown | 0.4268 |
| cagr | -0.1667 |
| net_avg_win | 88.9827 |
| net_avg_loss | -102.3016 |
| avg_hold_time_bars | 38.5756 |
| exposure | 0.7158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
