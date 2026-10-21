# EMA Hourly Continuation — BTT/USDT P21_200

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6155 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8549 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.2450 |
| sortino_ratio | -0.4900 |
| max_drawdown | 0.4563 |
| cagr | -0.2037 |
| net_avg_win | 63.4080 |
| net_avg_loss | -90.6528 |
| avg_hold_time_bars | 63.2000 |
| exposure | 0.6751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
