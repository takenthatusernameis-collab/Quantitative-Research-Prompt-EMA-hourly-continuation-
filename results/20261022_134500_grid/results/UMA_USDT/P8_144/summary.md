# EMA Hourly Continuation — UMA/USDT P8_144

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6469 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.8744 |
| sortino_ratio | -0.9691 |
| max_drawdown | 0.6936 |
| cagr | -0.3645 |
| net_avg_win | 45.1088 |
| net_avg_loss | -66.3694 |
| avg_hold_time_bars | 27.1749 |
| exposure | 0.6991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
