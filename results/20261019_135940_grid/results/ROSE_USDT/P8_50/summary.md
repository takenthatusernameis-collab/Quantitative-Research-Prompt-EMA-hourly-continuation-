# EMA Hourly Continuation — ROSE/USDT P8_50

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.6399 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 1.0232 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -5.5189 |
| sortino_ratio | -2.6301 |
| max_drawdown | 0.9607 |
| cagr | -0.7183 |
| net_avg_win | 30.9162 |
| net_avg_loss | -44.2922 |
| avg_hold_time_bars | 8.9453 |
| exposure | 0.4684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
