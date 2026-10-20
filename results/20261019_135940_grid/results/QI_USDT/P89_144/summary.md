# EMA Hourly Continuation — QI/USDT P89_144

**Symbol:** QI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.4303 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8120 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -4.8448 |
| sortino_ratio | -1.5051 |
| max_drawdown | 0.8345 |
| cagr | -0.5099 |
| net_avg_win | 29.1809 |
| net_avg_loss | -55.2768 |
| avg_hold_time_bars | 5.4740 |
| exposure | 0.1191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
