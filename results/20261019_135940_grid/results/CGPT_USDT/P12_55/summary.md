# EMA Hourly Continuation — CGPT/USDT P12_55

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.5717 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.9420 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -5.6828 |
| sortino_ratio | -2.4372 |
| max_drawdown | 0.9527 |
| cagr | -0.6963 |
| net_avg_win | 29.2774 |
| net_avg_loss | -44.0866 |
| avg_hold_time_bars | 8.9968 |
| exposure | 0.3828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
