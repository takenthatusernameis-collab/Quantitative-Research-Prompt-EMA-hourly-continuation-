# EMA Hourly Continuation — ANKR/USDT P21_144

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.5863 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -4.1819 |
| sortino_ratio | -1.2713 |
| max_drawdown | 0.7947 |
| cagr | -0.4644 |
| net_avg_win | 53.9205 |
| net_avg_loss | -71.6507 |
| avg_hold_time_bars | 27.2253 |
| exposure | 0.5878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
