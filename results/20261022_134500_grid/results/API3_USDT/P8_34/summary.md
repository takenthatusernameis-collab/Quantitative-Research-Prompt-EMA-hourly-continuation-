# EMA Hourly Continuation — API3/USDT P8_34

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1385 |
| net_profit_factor | 0.5392 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8891 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -8.3974 |
| sortino_ratio | -4.3937 |
| max_drawdown | 0.9954 |
| cagr | -0.8820 |
| net_avg_win | 18.8452 |
| net_avg_loss | -28.1611 |
| avg_hold_time_bars | 5.8051 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
