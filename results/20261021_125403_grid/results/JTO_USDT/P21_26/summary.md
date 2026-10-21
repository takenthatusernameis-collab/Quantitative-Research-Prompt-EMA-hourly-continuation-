# EMA Hourly Continuation — JTO/USDT P21_26

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.6978 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9509 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.7598 |
| sortino_ratio | -0.3944 |
| max_drawdown | 0.4045 |
| cagr | -0.1655 |
| net_avg_win | 70.8397 |
| net_avg_loss | -95.8782 |
| avg_hold_time_bars | 4.9143 |
| exposure | 0.0547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
