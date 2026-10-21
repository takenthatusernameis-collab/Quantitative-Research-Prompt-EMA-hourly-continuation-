# EMA Hourly Continuation — ROSE/USDT P8_26

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.7760 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -2.1212 |
| sortino_ratio | -0.8069 |
| max_drawdown | 0.6215 |
| cagr | -0.3099 |
| net_avg_win | 59.3069 |
| net_avg_loss | -77.7460 |
| avg_hold_time_bars | 6.2194 |
| exposure | 0.1985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
