# EMA Hourly Continuation — LTC/USDT P20_26

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.1371 |
| net_win_rate | 0.3114 |
| gross_profit_factor | 0.8133 |
| gross_win_rate | 0.3990 |
| sharpe_ratio | -17.0031 |
| sortino_ratio | -8.8444 |
| max_drawdown | 1.0000 |
| cagr | -0.9928 |
| net_avg_win | 4.2930 |
| net_avg_loss | -14.1667 |
| avg_hold_time_bars | 1.6776 |
| exposure | 0.0906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
