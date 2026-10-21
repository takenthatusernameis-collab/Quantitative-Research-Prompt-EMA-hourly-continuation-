# EMA Hourly Continuation — CTSI/USDT P21_55

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.6886 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9346 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -3.6454 |
| sortino_ratio | -1.3094 |
| max_drawdown | 0.7915 |
| cagr | -0.4517 |
| net_avg_win | 58.5961 |
| net_avg_loss | -73.5773 |
| avg_hold_time_bars | 7.8943 |
| exposure | 0.2275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
