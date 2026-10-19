# EMA Hourly Continuation — AR/USDT P12_26

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1449 |
| net_profit_factor | 0.4101 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.7755 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -10.6585 |
| sortino_ratio | -5.7140 |
| max_drawdown | 0.9992 |
| cagr | -0.9420 |
| net_avg_win | 11.2772 |
| net_avg_loss | -20.3348 |
| avg_hold_time_bars | 2.8875 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
