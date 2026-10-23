# EMA Hourly Continuation — STRAX/USDT P34_55

**Symbol:** STRAX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.3887 |
| net_win_rate | 0.3909 |
| gross_profit_factor | 0.7555 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -9.5788 |
| sortino_ratio | -4.0495 |
| max_drawdown | 0.9936 |
| cagr | -0.8679 |
| net_avg_win | 18.4715 |
| net_avg_loss | -30.4941 |
| avg_hold_time_bars | 4.8011 |
| exposure | 0.1921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
