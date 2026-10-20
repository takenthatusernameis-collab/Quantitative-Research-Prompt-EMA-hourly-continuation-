# EMA Hourly Continuation — T/USDT P34_100

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.5788 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9199 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -4.4114 |
| sortino_ratio | -1.4832 |
| max_drawdown | 0.8406 |
| cagr | -0.5102 |
| net_avg_win | 43.1244 |
| net_avg_loss | -64.5555 |
| avg_hold_time_bars | 11.0524 |
| exposure | 0.2866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
