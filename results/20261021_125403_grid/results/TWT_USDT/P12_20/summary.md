# EMA Hourly Continuation — TWT/USDT P12_20

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6550 |
| net_win_rate | 0.5186 |
| gross_profit_factor | 1.0781 |
| gross_win_rate | 0.5186 |
| sharpe_ratio | -2.5493 |
| sortino_ratio | -0.7142 |
| max_drawdown | 0.5657 |
| cagr | -0.2777 |
| net_avg_win | 54.3410 |
| net_avg_loss | -89.3856 |
| avg_hold_time_bars | 4.4069 |
| exposure | 0.0753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
