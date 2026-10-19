# EMA Hourly Continuation — DOT/USDT P21_55

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.5478 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.0065 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -5.6117 |
| sortino_ratio | -2.3697 |
| max_drawdown | 0.9488 |
| cagr | -0.6861 |
| net_avg_win | 26.0299 |
| net_avg_loss | -45.4525 |
| avg_hold_time_bars | 5.2278 |
| exposure | 0.2139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
