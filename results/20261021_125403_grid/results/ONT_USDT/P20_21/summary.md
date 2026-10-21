# EMA Hourly Continuation — ONT/USDT P20_21

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 181 |
| net_profit_factor | 0.5350 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8088 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -2.5036 |
| sortino_ratio | -0.4814 |
| max_drawdown | 0.4609 |
| cagr | -0.1989 |
| net_avg_win | 60.1204 |
| net_avg_loss | -93.0747 |
| avg_hold_time_bars | 5.2155 |
| exposure | 0.0427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
