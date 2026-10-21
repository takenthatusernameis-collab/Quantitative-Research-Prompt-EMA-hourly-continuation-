# EMA Hourly Continuation — AURORA/USDT P21_89

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9560 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -2.1941 |
| sortino_ratio | -0.6273 |
| max_drawdown | 0.5428 |
| cagr | -0.2501 |
| net_avg_win | 68.6720 |
| net_avg_loss | -89.2218 |
| avg_hold_time_bars | 19.9202 |
| exposure | 0.3631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
