# EMA Hourly Continuation — AR/USDT P55_144

**Symbol:** AR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6401 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9309 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.9971 |
| sortino_ratio | -0.9122 |
| max_drawdown | 0.6774 |
| cagr | -0.3537 |
| net_avg_win | 53.1183 |
| net_avg_loss | -75.5273 |
| avg_hold_time_bars | 12.1902 |
| exposure | 0.2593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
