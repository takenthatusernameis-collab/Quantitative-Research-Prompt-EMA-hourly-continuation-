# EMA Hourly Continuation — BDX/USDT P8_144

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1291 |
| net_profit_factor | 0.3006 |
| net_win_rate | 0.3098 |
| gross_profit_factor | 0.6386 |
| gross_win_rate | 0.3594 |
| sharpe_ratio | -15.8524 |
| sortino_ratio | -8.2506 |
| max_drawdown | 1.0000 |
| cagr | -0.9875 |
| net_avg_win | 10.7467 |
| net_avg_loss | -16.0477 |
| avg_hold_time_bars | 8.2758 |
| exposure | 0.4856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
