# EMA Hourly Continuation — TURBO/USDT P26_144

**Symbol:** TURBO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7603 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0287 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -2.1099 |
| sortino_ratio | -0.6885 |
| max_drawdown | 0.5423 |
| cagr | -0.2768 |
| net_avg_win | 70.3653 |
| net_avg_loss | -94.2477 |
| avg_hold_time_bars | 19.1136 |
| exposure | 0.4588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
