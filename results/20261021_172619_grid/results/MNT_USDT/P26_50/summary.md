# EMA Hourly Continuation — MNT/USDT P26_50

**Symbol:** MNT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.5769 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8753 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -3.4644 |
| sortino_ratio | -1.0052 |
| max_drawdown | 0.6912 |
| cagr | -0.3697 |
| net_avg_win | 48.7316 |
| net_avg_loss | -74.3988 |
| avg_hold_time_bars | 7.8073 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
