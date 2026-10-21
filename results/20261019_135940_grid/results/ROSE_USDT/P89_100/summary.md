# EMA Hourly Continuation — ROSE/USDT P89_100

**Symbol:** ROSE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.3077 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.7055 |
| gross_win_rate | 0.4235 |
| sharpe_ratio | -8.3807 |
| sortino_ratio | -2.9283 |
| max_drawdown | 0.9779 |
| cagr | -0.7799 |
| net_avg_win | 18.0287 |
| net_avg_loss | -39.8912 |
| avg_hold_time_bars | 2.1580 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
