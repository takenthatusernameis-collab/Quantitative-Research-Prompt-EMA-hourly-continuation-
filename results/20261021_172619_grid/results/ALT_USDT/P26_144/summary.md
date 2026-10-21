# EMA Hourly Continuation — ALT/USDT P26_144

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.7671 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.6775 |
| sortino_ratio | -0.4811 |
| max_drawdown | 0.4496 |
| cagr | -0.1999 |
| net_avg_win | 72.0623 |
| net_avg_loss | -88.0961 |
| avg_hold_time_bars | 25.7556 |
| exposure | 0.4741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
