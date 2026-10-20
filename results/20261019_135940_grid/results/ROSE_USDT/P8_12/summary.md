# EMA Hourly Continuation — ROSE/USDT P8_12

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1920 |
| net_profit_factor | 0.1653 |
| net_win_rate | 0.3823 |
| gross_profit_factor | 0.5765 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -16.9496 |
| sortino_ratio | -10.6204 |
| max_drawdown | 1.0000 |
| cagr | -0.9965 |
| net_avg_win | 2.6985 |
| net_avg_loss | -10.1018 |
| avg_hold_time_bars | 1.7099 |
| exposure | 0.1492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
