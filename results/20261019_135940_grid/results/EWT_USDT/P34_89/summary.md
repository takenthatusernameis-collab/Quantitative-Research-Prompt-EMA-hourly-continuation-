# EMA Hourly Continuation — EWT/USDT P34_89

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.4992 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.8044 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -6.0086 |
| sortino_ratio | -2.1680 |
| max_drawdown | 0.9338 |
| cagr | -0.6556 |
| net_avg_win | 32.6830 |
| net_avg_loss | -49.1907 |
| avg_hold_time_bars | 6.9864 |
| exposure | 0.2102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
