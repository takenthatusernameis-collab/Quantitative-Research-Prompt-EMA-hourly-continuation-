# EMA Hourly Continuation — CRV/USDT P21_26

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1187 |
| net_profit_factor | 0.2511 |
| net_win_rate | 0.3850 |
| gross_profit_factor | 0.7360 |
| gross_win_rate | 0.4212 |
| sharpe_ratio | -13.5097 |
| sortino_ratio | -6.7003 |
| max_drawdown | 0.9999 |
| cagr | -0.9733 |
| net_avg_win | 7.3365 |
| net_avg_loss | -18.2900 |
| avg_hold_time_bars | 1.7203 |
| exposure | 0.0928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
