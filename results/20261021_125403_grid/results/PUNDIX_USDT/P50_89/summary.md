# EMA Hourly Continuation — PUNDIX/USDT P50_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.5719 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8549 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.4222 |
| sortino_ratio | -0.9855 |
| max_drawdown | 0.6805 |
| cagr | -0.3628 |
| net_avg_win | 48.1498 |
| net_avg_loss | -72.9353 |
| avg_hold_time_bars | 9.3753 |
| exposure | 0.1726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
