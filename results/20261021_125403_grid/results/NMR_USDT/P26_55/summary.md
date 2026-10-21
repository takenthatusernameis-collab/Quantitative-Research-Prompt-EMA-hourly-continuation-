# EMA Hourly Continuation — NMR/USDT P26_55

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6494 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -3.5331 |
| sortino_ratio | -1.1489 |
| max_drawdown | 0.7407 |
| cagr | -0.4092 |
| net_avg_win | 56.5944 |
| net_avg_loss | -74.6973 |
| avg_hold_time_bars | 7.0538 |
| exposure | 0.1667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
