# EMA Hourly Continuation — SYN/USDT P55_200

**Symbol:** SYN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8050 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.8958 |
| sortino_ratio | -0.7870 |
| max_drawdown | 0.6219 |
| cagr | -0.3119 |
| net_avg_win | 51.2526 |
| net_avg_loss | -71.9519 |
| avg_hold_time_bars | 24.1524 |
| exposure | 0.4106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
