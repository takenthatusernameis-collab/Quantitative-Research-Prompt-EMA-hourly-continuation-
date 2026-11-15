# EMA Hourly Continuation — CERE/USDT P21_55

**Symbol:** CERE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.3649 |
| net_win_rate | 0.3317 |
| gross_profit_factor | 0.6831 |
| gross_win_rate | 0.3677 |
| sharpe_ratio | -12.8067 |
| sortino_ratio | -5.7829 |
| max_drawdown | 0.9995 |
| cagr | -0.9527 |
| net_avg_win | 17.3481 |
| net_avg_loss | -23.5945 |
| avg_hold_time_bars | 6.5641 |
| exposure | 0.2978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
