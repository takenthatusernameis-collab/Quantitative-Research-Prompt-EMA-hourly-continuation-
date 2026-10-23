# EMA Hourly Continuation — POKT/USDT P21_50

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.4639 |
| net_win_rate | 0.3996 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4122 |
| sharpe_ratio | -9.4890 |
| sortino_ratio | -4.4401 |
| max_drawdown | 0.9962 |
| cagr | -0.8896 |
| net_avg_win | 19.3273 |
| net_avg_loss | -27.7335 |
| avg_hold_time_bars | 4.8396 |
| exposure | 0.2444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
