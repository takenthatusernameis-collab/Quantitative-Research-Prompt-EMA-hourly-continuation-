# EMA Hourly Continuation — GMX/USDT P12_200

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7750 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -1.6548 |
| sortino_ratio | -0.4579 |
| max_drawdown | 0.4767 |
| cagr | -0.1912 |
| net_avg_win | 78.1735 |
| net_avg_loss | -93.1902 |
| avg_hold_time_bars | 40.7045 |
| exposure | 0.7012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
