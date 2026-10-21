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
| gross_profit_factor | 0.9110 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -6.1445 |
| sortino_ratio | -2.6633 |
| max_drawdown | 0.9626 |
| cagr | -0.7245 |
| net_avg_win | 23.5461 |
| net_avg_loss | -40.0105 |
| avg_hold_time_bars | 5.4815 |
| exposure | 0.2360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
