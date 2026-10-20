# EMA Hourly Continuation — REQ/USDT P20_26

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1361 |
| net_profit_factor | 0.2177 |
| net_win_rate | 0.3145 |
| gross_profit_factor | 0.7734 |
| gross_win_rate | 0.4063 |
| sharpe_ratio | -17.7939 |
| sortino_ratio | -9.8252 |
| max_drawdown | 1.0000 |
| cagr | -0.9949 |
| net_avg_win | 6.5006 |
| net_avg_loss | -13.7002 |
| avg_hold_time_bars | 2.3468 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
