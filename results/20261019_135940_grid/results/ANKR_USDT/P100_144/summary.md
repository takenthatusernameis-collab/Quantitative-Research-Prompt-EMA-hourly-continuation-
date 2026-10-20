# EMA Hourly Continuation — ANKR/USDT P100_144

**Symbol:** ANKR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.3952 |
| net_win_rate | 0.4113 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -6.6701 |
| sortino_ratio | -2.1195 |
| max_drawdown | 0.9293 |
| cagr | -0.6511 |
| net_avg_win | 29.7525 |
| net_avg_loss | -52.5985 |
| avg_hold_time_bars | 6.8609 |
| exposure | 0.1547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
