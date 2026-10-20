# EMA Hourly Continuation — LQTY/USDT P20_26

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1250 |
| net_profit_factor | 0.2894 |
| net_win_rate | 0.4088 |
| gross_profit_factor | 0.8172 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -12.4115 |
| sortino_ratio | -6.2682 |
| max_drawdown | 0.9997 |
| cagr | -0.9606 |
| net_avg_win | 7.9685 |
| net_avg_loss | -19.0380 |
| avg_hold_time_bars | 2.3024 |
| exposure | 0.1302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
