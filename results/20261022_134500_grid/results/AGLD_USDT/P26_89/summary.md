# EMA Hourly Continuation — AGLD/USDT P26_89

**Symbol:** AGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.6177 |
| net_win_rate | 0.4616 |
| gross_profit_factor | 0.9478 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -4.5699 |
| sortino_ratio | -1.7344 |
| max_drawdown | 0.8806 |
| cagr | -0.5609 |
| net_avg_win | 41.9260 |
| net_avg_loss | -58.2054 |
| avg_hold_time_bars | 10.0589 |
| exposure | 0.3323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
