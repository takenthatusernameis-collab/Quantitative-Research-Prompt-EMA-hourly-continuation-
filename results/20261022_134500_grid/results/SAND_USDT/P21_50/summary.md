# EMA Hourly Continuation — SAND/USDT P21_50

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.4760 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -7.5863 |
| sortino_ratio | -3.2445 |
| max_drawdown | 0.9833 |
| cagr | -0.8011 |
| net_avg_win | 21.6146 |
| net_avg_loss | -36.5566 |
| avg_hold_time_bars | 4.8467 |
| exposure | 0.2040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
