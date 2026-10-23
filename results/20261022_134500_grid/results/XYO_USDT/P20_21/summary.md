# EMA Hourly Continuation — XYO/USDT P20_21

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1318 |
| net_profit_factor | 0.1109 |
| net_win_rate | 0.2633 |
| gross_profit_factor | 0.6381 |
| gross_win_rate | 0.3445 |
| sharpe_ratio | -19.7846 |
| sortino_ratio | -11.0399 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 3.5946 |
| net_avg_loss | -11.5832 |
| avg_hold_time_bars | 2.0296 |
| exposure | 0.1210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
