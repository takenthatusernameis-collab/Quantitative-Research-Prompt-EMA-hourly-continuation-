# EMA Hourly Continuation — AGLD/USDT P8_12

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5836 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.7822 |
| sortino_ratio | -1.2726 |
| max_drawdown | 0.7693 |
| cagr | -0.4410 |
| net_avg_win | 41.1512 |
| net_avg_loss | -63.7071 |
| avg_hold_time_bars | 4.6304 |
| exposure | 0.1157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
