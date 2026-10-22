# EMA Hourly Continuation — STRK/USDT P26_144

**Symbol:** STRK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9349 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -2.8668 |
| sortino_ratio | -0.8934 |
| max_drawdown | 0.6897 |
| cagr | -0.3439 |
| net_avg_win | 62.5634 |
| net_avg_loss | -81.7187 |
| avg_hold_time_bars | 21.2901 |
| exposure | 0.4703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
