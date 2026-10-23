# EMA Hourly Continuation — UMA/USDT P8_12

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1725 |
| net_profit_factor | 0.2249 |
| net_win_rate | 0.3722 |
| gross_profit_factor | 0.7194 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -16.5463 |
| sortino_ratio | -9.9296 |
| max_drawdown | 1.0000 |
| cagr | -0.9942 |
| net_avg_win | 4.5193 |
| net_avg_loss | -11.9126 |
| avg_hold_time_bars | 2.3391 |
| exposure | 0.1834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
