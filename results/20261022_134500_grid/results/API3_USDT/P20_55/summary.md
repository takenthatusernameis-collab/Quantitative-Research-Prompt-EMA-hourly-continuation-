# EMA Hourly Continuation — API3/USDT P20_55

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -6.0718 |
| sortino_ratio | -2.6878 |
| max_drawdown | 0.9616 |
| cagr | -0.7209 |
| net_avg_win | 31.3566 |
| net_avg_loss | -45.2119 |
| avg_hold_time_bars | 5.6158 |
| exposure | 0.2491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
