# EMA Hourly Continuation — SAFE/USDT P8_34

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.4668 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8270 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -7.1660 |
| sortino_ratio | -3.6048 |
| max_drawdown | 0.9880 |
| cagr | -0.8262 |
| net_avg_win | 14.6249 |
| net_avg_loss | -27.0697 |
| avg_hold_time_bars | 6.1286 |
| exposure | 0.3578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
