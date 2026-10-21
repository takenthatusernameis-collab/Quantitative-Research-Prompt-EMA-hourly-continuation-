# EMA Hourly Continuation — ROSE/USDT P55_200

**Symbol:** ROSE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7331 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0521 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -1.6850 |
| sortino_ratio | -0.4615 |
| max_drawdown | 0.4662 |
| cagr | -0.1984 |
| net_avg_win | 60.9755 |
| net_avg_loss | -87.2633 |
| avg_hold_time_bars | 23.2107 |
| exposure | 0.3956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
