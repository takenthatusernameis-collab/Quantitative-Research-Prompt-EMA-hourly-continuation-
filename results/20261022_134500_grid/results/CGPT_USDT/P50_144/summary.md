# EMA Hourly Continuation — CGPT/USDT P50_144

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.5863 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8607 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -3.7007 |
| sortino_ratio | -1.1378 |
| max_drawdown | 0.7530 |
| cagr | -0.4246 |
| net_avg_win | 48.1300 |
| net_avg_loss | -69.5067 |
| avg_hold_time_bars | 12.9979 |
| exposure | 0.2848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
