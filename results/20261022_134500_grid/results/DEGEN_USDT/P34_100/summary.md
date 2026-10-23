# EMA Hourly Continuation — DEGEN/USDT P34_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.7396 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 1.0150 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -2.7665 |
| sortino_ratio | -0.9832 |
| max_drawdown | 0.6956 |
| cagr | -0.3686 |
| net_avg_win | 63.1054 |
| net_avg_loss | -83.1620 |
| avg_hold_time_bars | 9.6987 |
| exposure | 0.2755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
