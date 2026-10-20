# EMA Hourly Continuation — YFI/USDT P20_26

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1363 |
| net_profit_factor | 0.1709 |
| net_win_rate | 0.3243 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -17.4327 |
| sortino_ratio | -9.5732 |
| max_drawdown | 1.0000 |
| cagr | -0.9942 |
| net_avg_win | 4.6643 |
| net_avg_loss | -13.0962 |
| avg_hold_time_bars | 2.1731 |
| exposure | 0.1340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
