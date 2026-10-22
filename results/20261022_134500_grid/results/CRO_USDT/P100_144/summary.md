# EMA Hourly Continuation — CRO/USDT P100_144

**Symbol:** CRO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.3115 |
| net_win_rate | 0.4093 |
| gross_profit_factor | 0.7675 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -7.2785 |
| sortino_ratio | -2.3218 |
| max_drawdown | 0.9484 |
| cagr | -0.6926 |
| net_avg_win | 21.1370 |
| net_avg_loss | -47.0092 |
| avg_hold_time_bars | 4.1573 |
| exposure | 0.0937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
