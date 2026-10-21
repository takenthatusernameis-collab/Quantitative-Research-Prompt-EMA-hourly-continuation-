# EMA Hourly Continuation — JTO/USDT P26_55

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7191 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.3977 |
| sortino_ratio | -0.7462 |
| max_drawdown | 0.5954 |
| cagr | -0.2904 |
| net_avg_win | 65.3968 |
| net_avg_loss | -82.2164 |
| avg_hold_time_bars | 7.4748 |
| exposure | 0.1617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
