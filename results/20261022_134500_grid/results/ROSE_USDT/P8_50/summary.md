# EMA Hourly Continuation — ROSE/USDT P8_50

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.6403 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -5.5101 |
| sortino_ratio | -2.6260 |
| max_drawdown | 0.9607 |
| cagr | -0.7178 |
| net_avg_win | 30.9065 |
| net_avg_loss | -44.4053 |
| avg_hold_time_bars | 8.9462 |
| exposure | 0.4685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
