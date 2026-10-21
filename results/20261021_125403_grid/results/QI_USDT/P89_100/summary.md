# EMA Hourly Continuation — QI/USDT P89_100

**Symbol:** QI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.6076 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9625 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -1.8662 |
| sortino_ratio | -0.3335 |
| max_drawdown | 0.3375 |
| cagr | -0.1423 |
| net_avg_win | 64.5687 |
| net_avg_loss | -103.5757 |
| avg_hold_time_bars | 6.7821 |
| exposure | 0.0479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
