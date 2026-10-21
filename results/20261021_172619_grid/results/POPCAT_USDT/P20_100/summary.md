# EMA Hourly Continuation — POPCAT/USDT P20_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7288 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8559 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.1272 |
| sortino_ratio | -0.6433 |
| max_drawdown | 0.4848 |
| cagr | -0.2570 |
| net_avg_win | 70.3388 |
| net_avg_loss | -83.1818 |
| avg_hold_time_bars | 20.3683 |
| exposure | 0.4207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
