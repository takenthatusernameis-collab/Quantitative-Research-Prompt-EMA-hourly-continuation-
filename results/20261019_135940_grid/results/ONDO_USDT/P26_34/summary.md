# EMA Hourly Continuation — ONDO/USDT P26_34

**Symbol:** ONDO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1062 |
| net_profit_factor | 0.3307 |
| net_win_rate | 0.4002 |
| gross_profit_factor | 0.7896 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -11.6543 |
| sortino_ratio | -5.4241 |
| max_drawdown | 0.9992 |
| cagr | -0.9413 |
| net_avg_win | 11.6169 |
| net_avg_loss | -23.4366 |
| avg_hold_time_bars | 2.0169 |
| exposure | 0.0974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
