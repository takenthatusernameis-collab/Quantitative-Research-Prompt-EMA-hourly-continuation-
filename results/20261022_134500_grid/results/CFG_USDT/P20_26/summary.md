# EMA Hourly Continuation — CFG/USDT P20_26

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.1749 |
| net_win_rate | 0.3397 |
| gross_profit_factor | 0.4941 |
| gross_win_rate | 0.3659 |
| sharpe_ratio | -12.7399 |
| sortino_ratio | -5.7913 |
| max_drawdown | 0.9995 |
| cagr | -0.9507 |
| net_avg_win | 6.2865 |
| net_avg_loss | -18.4937 |
| avg_hold_time_bars | 6.6381 |
| exposure | 0.2993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
