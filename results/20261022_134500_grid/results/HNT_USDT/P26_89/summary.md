# EMA Hourly Continuation — HNT/USDT P26_89

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.5644 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8490 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -4.9878 |
| sortino_ratio | -1.9332 |
| max_drawdown | 0.9115 |
| cagr | -0.6060 |
| net_avg_win | 33.8347 |
| net_avg_loss | -50.4692 |
| avg_hold_time_bars | 9.1559 |
| exposure | 0.3150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
