# EMA Hourly Continuation — EUL/USDT P21_34

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.5442 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.7663 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -3.0945 |
| sortino_ratio | -0.8134 |
| max_drawdown | 0.6180 |
| cagr | -0.3119 |
| net_avg_win | 47.5203 |
| net_avg_loss | -71.4418 |
| avg_hold_time_bars | 7.0029 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
