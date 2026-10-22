# EMA Hourly Continuation — DBR/USDT P34_89

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.4833 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.8679 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -5.7038 |
| sortino_ratio | -1.9555 |
| max_drawdown | 0.8585 |
| cagr | -0.6122 |
| net_avg_win | 38.6232 |
| net_avg_loss | -61.8911 |
| avg_hold_time_bars | 8.8983 |
| exposure | 0.2388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
