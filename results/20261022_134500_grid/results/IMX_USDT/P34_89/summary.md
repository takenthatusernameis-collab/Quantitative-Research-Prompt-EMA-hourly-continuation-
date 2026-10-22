# EMA Hourly Continuation — IMX/USDT P34_89

**Symbol:** IMX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.6046 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9287 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -4.0577 |
| sortino_ratio | -1.5087 |
| max_drawdown | 0.8465 |
| cagr | -0.5212 |
| net_avg_win | 37.6279 |
| net_avg_loss | -58.6436 |
| avg_hold_time_bars | 7.2037 |
| exposure | 0.2305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
