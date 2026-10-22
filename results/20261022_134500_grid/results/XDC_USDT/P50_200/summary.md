# EMA Hourly Continuation — XDC/USDT P50_200

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.4111 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8260 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.6755 |
| sortino_ratio | -1.8301 |
| max_drawdown | 0.9079 |
| cagr | -0.6098 |
| net_avg_win | 26.5696 |
| net_avg_loss | -51.6201 |
| avg_hold_time_bars | 12.3582 |
| exposure | 0.3011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
