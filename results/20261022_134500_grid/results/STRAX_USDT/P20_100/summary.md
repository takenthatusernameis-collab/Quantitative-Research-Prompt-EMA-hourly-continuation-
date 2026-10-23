# EMA Hourly Continuation — STRAX/USDT P20_100

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.5361 |
| net_win_rate | 0.4107 |
| gross_profit_factor | 0.7988 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -6.9579 |
| sortino_ratio | -2.7045 |
| max_drawdown | 0.9650 |
| cagr | -0.7362 |
| net_avg_win | 35.3757 |
| net_avg_loss | -45.9831 |
| avg_hold_time_bars | 11.7158 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
