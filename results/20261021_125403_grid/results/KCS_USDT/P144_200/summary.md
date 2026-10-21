# EMA Hourly Continuation — KCS/USDT P144_200

**Symbol:** KCS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.4246 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8623 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -3.5875 |
| sortino_ratio | -0.7478 |
| max_drawdown | 0.5823 |
| cagr | -0.2912 |
| net_avg_win | 45.9063 |
| net_avg_loss | -88.2065 |
| avg_hold_time_bars | 7.3043 |
| exposure | 0.0687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
