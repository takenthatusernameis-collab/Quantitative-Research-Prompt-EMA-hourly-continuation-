# EMA Hourly Continuation — DGB/USDT P26_100

**Symbol:** DGB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8796 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -6.3869 |
| sortino_ratio | -2.4342 |
| max_drawdown | 0.9546 |
| cagr | -0.7080 |
| net_avg_win | 32.9160 |
| net_avg_loss | -47.9062 |
| avg_hold_time_bars | 10.4365 |
| exposure | 0.3586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
