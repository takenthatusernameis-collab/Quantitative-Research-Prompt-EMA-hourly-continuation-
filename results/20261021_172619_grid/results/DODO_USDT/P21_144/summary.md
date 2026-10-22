# EMA Hourly Continuation — DODO/USDT P21_144

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.6630 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.8133 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -3.0106 |
| sortino_ratio | -0.8775 |
| max_drawdown | 0.6652 |
| cagr | -0.3321 |
| net_avg_win | 67.5535 |
| net_avg_loss | -78.6399 |
| avg_hold_time_bars | 26.4918 |
| exposure | 0.5119 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
