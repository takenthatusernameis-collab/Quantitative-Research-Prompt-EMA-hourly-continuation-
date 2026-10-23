# EMA Hourly Continuation — WIN/USDT P21_34

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.2223 |
| net_win_rate | 0.3558 |
| gross_profit_factor | 0.7119 |
| gross_win_rate | 0.3904 |
| sharpe_ratio | -14.1143 |
| sortino_ratio | -6.7989 |
| max_drawdown | 0.9999 |
| cagr | -0.9725 |
| net_avg_win | 7.5232 |
| net_avg_loss | -18.6884 |
| avg_hold_time_bars | 2.7247 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
