# EMA Hourly Continuation — ROSE/USDT P26_144

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.9473 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1290 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.2956 |
| sortino_ratio | -0.0842 |
| max_drawdown | 0.2561 |
| cagr | -0.0435 |
| net_avg_win | 91.2788 |
| net_avg_loss | -110.1273 |
| avg_hold_time_bars | 27.3359 |
| exposure | 0.4846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
