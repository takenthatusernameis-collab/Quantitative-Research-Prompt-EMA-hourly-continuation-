# EMA Hourly Continuation — MNT/USDT P50_55

**Symbol:** MNT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.4824 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.7869 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -2.6144 |
| sortino_ratio | -0.4443 |
| max_drawdown | 0.4218 |
| cagr | -0.1864 |
| net_avg_win | 60.7794 |
| net_avg_loss | -100.1468 |
| avg_hold_time_bars | 5.0429 |
| exposure | 0.0321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
