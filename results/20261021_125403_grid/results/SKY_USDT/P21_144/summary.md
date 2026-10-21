# EMA Hourly Continuation — SKY/USDT P21_144

**Symbol:** SKY/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8547 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0543 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -0.8970 |
| sortino_ratio | -0.2453 |
| max_drawdown | 0.4006 |
| cagr | -0.1088 |
| net_avg_win | 80.7408 |
| net_avg_loss | -101.0731 |
| avg_hold_time_bars | 33.3480 |
| exposure | 0.5504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
