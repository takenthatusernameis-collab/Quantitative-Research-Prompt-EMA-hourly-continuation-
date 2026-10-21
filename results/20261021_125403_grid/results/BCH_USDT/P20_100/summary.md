# EMA Hourly Continuation — BCH/USDT P20_100

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7059 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.4827 |
| sortino_ratio | -0.7366 |
| max_drawdown | 0.5967 |
| cagr | -0.2872 |
| net_avg_win | 66.7364 |
| net_avg_loss | -86.1684 |
| avg_hold_time_bars | 21.4120 |
| exposure | 0.4205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
