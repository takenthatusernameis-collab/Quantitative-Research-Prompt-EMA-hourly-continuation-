# EMA Hourly Continuation — UMA/USDT P55_144

**Symbol:** UMA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6018 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9594 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -3.3398 |
| sortino_ratio | -1.0498 |
| max_drawdown | 0.7266 |
| cagr | -0.3936 |
| net_avg_win | 44.6625 |
| net_avg_loss | -70.1608 |
| avg_hold_time_bars | 11.4920 |
| exposure | 0.2601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
