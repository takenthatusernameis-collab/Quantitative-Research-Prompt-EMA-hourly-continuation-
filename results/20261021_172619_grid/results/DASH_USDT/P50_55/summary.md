# EMA Hourly Continuation — DASH/USDT P50_55

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 76 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.0901 |
| sortino_ratio | -0.1363 |
| max_drawdown | 0.1861 |
| cagr | -0.0602 |
| net_avg_win | 80.8915 |
| net_avg_loss | -113.7858 |
| avg_hold_time_bars | 4.9474 |
| exposure | 0.0171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
