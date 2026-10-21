# EMA Hourly Continuation — LTC/USDT P100_144

**Symbol:** LTC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9166 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -2.2115 |
| sortino_ratio | -0.4456 |
| max_drawdown | 0.4280 |
| cagr | -0.1834 |
| net_avg_win | 57.8690 |
| net_avg_loss | -93.9108 |
| avg_hold_time_bars | 6.3214 |
| exposure | 0.0563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
