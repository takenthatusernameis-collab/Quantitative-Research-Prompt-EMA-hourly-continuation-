# EMA Hourly Continuation — TRB/USDT P100_144

**Symbol:** TRB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.5961 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8257 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -2.4589 |
| sortino_ratio | -0.5484 |
| max_drawdown | 0.4943 |
| cagr | -0.2237 |
| net_avg_win | 62.2067 |
| net_avg_loss | -87.2202 |
| avg_hold_time_bars | 6.1504 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
