# EMA Hourly Continuation — NOT/USDT P34_100

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7925 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9707 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -1.4783 |
| sortino_ratio | -0.4262 |
| max_drawdown | 0.4335 |
| cagr | -0.1788 |
| net_avg_win | 74.9115 |
| net_avg_loss | -92.1481 |
| avg_hold_time_bars | 14.7506 |
| exposure | 0.2723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
