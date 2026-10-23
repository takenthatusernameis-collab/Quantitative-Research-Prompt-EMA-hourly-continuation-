# EMA Hourly Continuation — NYM/USDT P89_144

**Symbol:** NYM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.2225 |
| net_win_rate | 0.3284 |
| gross_profit_factor | 0.5888 |
| gross_win_rate | 0.3642 |
| sharpe_ratio | -9.3106 |
| sortino_ratio | -2.9689 |
| max_drawdown | 0.9812 |
| cagr | -0.7946 |
| net_avg_win | 18.0033 |
| net_avg_loss | -39.5636 |
| avg_hold_time_bars | 6.3284 |
| exposure | 0.1366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
