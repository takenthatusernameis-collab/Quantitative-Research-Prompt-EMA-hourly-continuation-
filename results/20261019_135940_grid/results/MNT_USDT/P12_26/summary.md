# EMA Hourly Continuation — MNT/USDT P12_26

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1362 |
| net_profit_factor | 0.2916 |
| net_win_rate | 0.3767 |
| gross_profit_factor | 0.7923 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -13.8759 |
| sortino_ratio | -7.3439 |
| max_drawdown | 0.9999 |
| cagr | -0.9789 |
| net_avg_win | 8.0228 |
| net_avg_loss | -16.6255 |
| avg_hold_time_bars | 3.5742 |
| exposure | 0.2213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
