# EMA Hourly Continuation — ORCA/USDT P34_144

**Symbol:** ORCA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.5937 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.8807 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -3.0675 |
| sortino_ratio | -0.9240 |
| max_drawdown | 0.6824 |
| cagr | -0.3548 |
| net_avg_win | 45.5699 |
| net_avg_loss | -67.0394 |
| avg_hold_time_bars | 19.4227 |
| exposure | 0.4052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
