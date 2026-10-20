# EMA Hourly Continuation — MERL/USDT P100_144

**Symbol:** MERL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5686 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8757 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -4.2394 |
| sortino_ratio | -1.2944 |
| max_drawdown | 0.8050 |
| cagr | -0.4628 |
| net_avg_win | 49.2857 |
| net_avg_loss | -71.4451 |
| avg_hold_time_bars | 4.1199 |
| exposure | 0.0877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
