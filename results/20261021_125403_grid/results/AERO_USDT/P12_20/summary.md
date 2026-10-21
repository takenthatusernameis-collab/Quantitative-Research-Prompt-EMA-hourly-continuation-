# EMA Hourly Continuation — AERO/USDT P12_20

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.8192 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1013 |
| gross_win_rate | 0.5299 |
| sharpe_ratio | -0.9015 |
| sortino_ratio | -0.2131 |
| max_drawdown | 0.2971 |
| cagr | -0.0938 |
| net_avg_win | 69.9550 |
| net_avg_loss | -96.2328 |
| avg_hold_time_bars | 4.9179 |
| exposure | 0.0599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
