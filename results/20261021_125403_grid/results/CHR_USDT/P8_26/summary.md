# EMA Hourly Continuation — CHR/USDT P8_26

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.7566 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.7502 |
| sortino_ratio | -1.1031 |
| max_drawdown | 0.7316 |
| cagr | -0.3965 |
| net_avg_win | 57.5421 |
| net_avg_loss | -74.3381 |
| avg_hold_time_bars | 6.7649 |
| exposure | 0.2409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
