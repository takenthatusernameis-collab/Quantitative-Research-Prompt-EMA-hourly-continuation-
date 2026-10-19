# EMA Hourly Continuation — AKT/USDT P8_26

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1481 |
| net_profit_factor | 0.4907 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -9.5348 |
| sortino_ratio | -5.1310 |
| max_drawdown | 0.9985 |
| cagr | -0.9230 |
| net_avg_win | 14.6637 |
| net_avg_loss | -23.7617 |
| avg_hold_time_bars | 3.6894 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
