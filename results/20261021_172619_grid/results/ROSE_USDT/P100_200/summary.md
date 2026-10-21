# EMA Hourly Continuation — ROSE/USDT P100_200

**Symbol:** ROSE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8990 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1073 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.4699 |
| sortino_ratio | -0.1114 |
| max_drawdown | 0.1852 |
| cagr | -0.0528 |
| net_avg_win | 79.2136 |
| net_avg_loss | -99.2123 |
| avg_hold_time_bars | 12.2444 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
