# EMA Hourly Continuation — RLC/USDT P20_55

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.5217 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -6.1382 |
| sortino_ratio | -2.6609 |
| max_drawdown | 0.9626 |
| cagr | -0.7241 |
| net_avg_win | 23.5463 |
| net_avg_loss | -40.0084 |
| avg_hold_time_bars | 5.4805 |
| exposure | 0.2359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
