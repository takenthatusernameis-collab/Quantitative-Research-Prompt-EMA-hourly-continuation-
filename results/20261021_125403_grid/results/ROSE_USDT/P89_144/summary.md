# EMA Hourly Continuation — ROSE/USDT P89_144

**Symbol:** ROSE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8270 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0649 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.9062 |
| sortino_ratio | -0.2164 |
| max_drawdown | 0.2377 |
| cagr | -0.0958 |
| net_avg_win | 74.7535 |
| net_avg_loss | -97.9189 |
| avg_hold_time_bars | 7.5055 |
| exposure | 0.0938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
