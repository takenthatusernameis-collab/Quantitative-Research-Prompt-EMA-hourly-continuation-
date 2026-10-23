# EMA Hourly Continuation — XYO/USDT P20_100

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.4425 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.7656 |
| gross_win_rate | 0.4178 |
| sharpe_ratio | -7.7700 |
| sortino_ratio | -3.0905 |
| max_drawdown | 0.9790 |
| cagr | -0.7805 |
| net_avg_win | 24.1891 |
| net_avg_loss | -36.8625 |
| avg_hold_time_bars | 11.8407 |
| exposure | 0.4270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
