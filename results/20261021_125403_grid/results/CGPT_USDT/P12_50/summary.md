# EMA Hourly Continuation — CGPT/USDT P12_50

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.7737 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.9775 |
| sortino_ratio | -0.6948 |
| max_drawdown | 0.6059 |
| cagr | -0.2741 |
| net_avg_win | 63.4000 |
| net_avg_loss | -80.0664 |
| avg_hold_time_bars | 11.3284 |
| exposure | 0.3105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
