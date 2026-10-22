# EMA Hourly Continuation — STRAX/USDT P8_55

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.6864 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9161 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -4.0041 |
| sortino_ratio | -1.5637 |
| max_drawdown | 0.8469 |
| cagr | -0.5142 |
| net_avg_win | 52.6889 |
| net_avg_loss | -65.9265 |
| avg_hold_time_bars | 13.1039 |
| exposure | 0.4499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
