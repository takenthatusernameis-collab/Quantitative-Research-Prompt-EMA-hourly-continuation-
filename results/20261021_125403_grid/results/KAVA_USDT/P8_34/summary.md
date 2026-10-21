# EMA Hourly Continuation — KAVA/USDT P8_34

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.6470 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.9265 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -4.8381 |
| sortino_ratio | -1.9522 |
| max_drawdown | 0.9026 |
| cagr | -0.5974 |
| net_avg_win | 44.4981 |
| net_avg_loss | -58.9030 |
| avg_hold_time_bars | 8.9713 |
| exposure | 0.3270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
