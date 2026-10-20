# EMA Hourly Continuation — LSK/USDT P50_55

**Symbol:** LSK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.2232 |
| net_win_rate | 0.3741 |
| gross_profit_factor | 0.7854 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -10.4628 |
| sortino_ratio | -4.0436 |
| max_drawdown | 0.9956 |
| cagr | -0.8843 |
| net_avg_win | 10.8757 |
| net_avg_loss | -29.1271 |
| avg_hold_time_bars | 3.1181 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
