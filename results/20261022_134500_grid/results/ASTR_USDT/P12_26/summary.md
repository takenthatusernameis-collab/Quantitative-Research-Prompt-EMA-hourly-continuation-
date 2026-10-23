# EMA Hourly Continuation — ASTR/USDT P12_26

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1266 |
| net_profit_factor | 0.4046 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.9383 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -9.9452 |
| sortino_ratio | -4.9841 |
| max_drawdown | 0.9982 |
| cagr | -0.9188 |
| net_avg_win | 12.0284 |
| net_avg_loss | -23.8835 |
| avg_hold_time_bars | 3.8136 |
| exposure | 0.2185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
