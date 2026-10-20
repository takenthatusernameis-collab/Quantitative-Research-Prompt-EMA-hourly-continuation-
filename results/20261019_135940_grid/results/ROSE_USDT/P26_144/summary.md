# EMA Hourly Continuation — ROSE/USDT P26_144

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7648 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0624 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -2.0782 |
| sortino_ratio | -0.6475 |
| max_drawdown | 0.6026 |
| cagr | -0.2682 |
| net_avg_win | 71.2612 |
| net_avg_loss | -93.9312 |
| avg_hold_time_bars | 21.9777 |
| exposure | 0.4935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
