# EMA Hourly Continuation — ALT/USDT P89_144

**Symbol:** ALT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5416 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -3.9547 |
| sortino_ratio | -1.1926 |
| max_drawdown | 0.7597 |
| cagr | -0.4299 |
| net_avg_win | 43.3654 |
| net_avg_loss | -66.7788 |
| avg_hold_time_bars | 6.9691 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
