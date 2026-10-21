# EMA Hourly Continuation — DIA/USDT P20_55

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6424 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8521 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -3.6001 |
| sortino_ratio | -1.2462 |
| max_drawdown | 0.7767 |
| cagr | -0.4366 |
| net_avg_win | 50.7077 |
| net_avg_loss | -66.2230 |
| avg_hold_time_bars | 8.1582 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
