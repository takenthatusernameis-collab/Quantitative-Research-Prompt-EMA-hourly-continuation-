# EMA Hourly Continuation — LQTY/USDT P12_21

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1455 |
| net_profit_factor | 0.3458 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.8468 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -11.3710 |
| sortino_ratio | -6.1171 |
| max_drawdown | 0.9996 |
| cagr | -0.9548 |
| net_avg_win | 8.3885 |
| net_avg_loss | -18.5221 |
| avg_hold_time_bars | 2.7746 |
| exposure | 0.1827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
