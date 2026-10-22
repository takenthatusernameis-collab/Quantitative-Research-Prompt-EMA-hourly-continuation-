# EMA Hourly Continuation — JTO/USDT P8_200

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8488 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0922 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -1.0034 |
| sortino_ratio | -0.2817 |
| max_drawdown | 0.4135 |
| cagr | -0.1264 |
| net_avg_win | 79.9611 |
| net_avg_loss | -100.6895 |
| avg_hold_time_bars | 44.2276 |
| exposure | 0.7860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
