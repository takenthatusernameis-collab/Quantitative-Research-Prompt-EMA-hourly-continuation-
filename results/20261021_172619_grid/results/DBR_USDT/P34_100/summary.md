# EMA Hourly Continuation — DBR/USDT P34_100

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6397 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.8930 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -2.7414 |
| sortino_ratio | -0.7626 |
| max_drawdown | 0.5294 |
| cagr | -0.2952 |
| net_avg_win | 62.2026 |
| net_avg_loss | -86.9742 |
| avg_hold_time_bars | 14.1705 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
