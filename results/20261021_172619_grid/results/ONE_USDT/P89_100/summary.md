# EMA Hourly Continuation — ONE/USDT P89_100

**Symbol:** ONE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 86 |
| net_profit_factor | 1.0750 |
| net_win_rate | 0.5930 |
| gross_profit_factor | 1.4389 |
| gross_win_rate | 0.5930 |
| sharpe_ratio | 0.2433 |
| sortino_ratio | 0.0333 |
| max_drawdown | 0.0581 |
| cagr | 0.0125 |
| net_avg_win | 89.1664 |
| net_avg_loss | -120.8659 |
| avg_hold_time_bars | 6.8953 |
| exposure | 0.0270 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
