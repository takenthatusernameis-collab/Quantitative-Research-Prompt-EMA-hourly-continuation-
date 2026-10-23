# EMA Hourly Continuation — STRAX/USDT P26_55

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.5145 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -8.0652 |
| sortino_ratio | -3.4648 |
| max_drawdown | 0.9863 |
| cagr | -0.8192 |
| net_avg_win | 26.7293 |
| net_avg_loss | -38.4687 |
| avg_hold_time_bars | 5.9543 |
| exposure | 0.2502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
