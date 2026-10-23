# EMA Hourly Continuation — ENJ/USDT P50_144

**Symbol:** ENJ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.5829 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -3.6979 |
| sortino_ratio | -1.1116 |
| max_drawdown | 0.7492 |
| cagr | -0.4191 |
| net_avg_win | 47.8232 |
| net_avg_loss | -72.4077 |
| avg_hold_time_bars | 15.5505 |
| exposure | 0.3272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
