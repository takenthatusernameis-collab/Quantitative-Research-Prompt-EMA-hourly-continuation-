# EMA Hourly Continuation — ETC/USDT P20_21

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1247 |
| net_profit_factor | 0.1162 |
| net_win_rate | 0.2374 |
| gross_profit_factor | 0.8079 |
| gross_win_rate | 0.3504 |
| sharpe_ratio | -21.0006 |
| sortino_ratio | -12.0885 |
| max_drawdown | 1.0000 |
| cagr | -0.9989 |
| net_avg_win | 4.4416 |
| net_avg_loss | -11.8977 |
| avg_hold_time_bars | 1.4683 |
| exposure | 0.0832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
