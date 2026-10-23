# EMA Hourly Continuation — DGB/USDT P8_21

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1796 |
| net_profit_factor | 0.3851 |
| net_win_rate | 0.4026 |
| gross_profit_factor | 0.9232 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -14.0875 |
| sortino_ratio | -8.4374 |
| max_drawdown | 1.0000 |
| cagr | -0.9870 |
| net_avg_win | 8.6627 |
| net_avg_loss | -15.1566 |
| avg_hold_time_bars | 2.8118 |
| exposure | 0.2295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
