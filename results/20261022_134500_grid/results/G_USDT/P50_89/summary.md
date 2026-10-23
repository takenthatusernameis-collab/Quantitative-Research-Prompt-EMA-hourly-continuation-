# EMA Hourly Continuation — G/USDT P50_89

**Symbol:** G/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.4733 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8700 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -5.3021 |
| sortino_ratio | -1.8754 |
| max_drawdown | 0.8573 |
| cagr | -0.5880 |
| net_avg_win | 31.5894 |
| net_avg_loss | -56.1160 |
| avg_hold_time_bars | 6.0019 |
| exposure | 0.1679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
