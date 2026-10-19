# EMA Hourly Continuation — ENA/USDT P12_21

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1495 |
| net_profit_factor | 0.3965 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7766 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -10.4131 |
| sortino_ratio | -5.6953 |
| max_drawdown | 0.9992 |
| cagr | -0.9415 |
| net_avg_win | 10.0684 |
| net_avg_loss | -19.6400 |
| avg_hold_time_bars | 2.1967 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
