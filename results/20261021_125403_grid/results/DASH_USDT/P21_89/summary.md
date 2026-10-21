# EMA Hourly Continuation — DASH/USDT P21_89

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7515 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9844 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.9422 |
| sortino_ratio | -0.5954 |
| max_drawdown | 0.5729 |
| cagr | -0.2388 |
| net_avg_win | 66.3618 |
| net_avg_loss | -85.6565 |
| avg_hold_time_bars | 16.5969 |
| exposure | 0.3463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
