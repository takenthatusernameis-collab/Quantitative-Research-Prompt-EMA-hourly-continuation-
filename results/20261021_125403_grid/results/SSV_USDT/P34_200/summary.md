# EMA Hourly Continuation — SSV/USDT P34_200

**Symbol:** SSV/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8611 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -0.7605 |
| sortino_ratio | -0.1846 |
| max_drawdown | 0.2547 |
| cagr | -0.0834 |
| net_avg_win | 82.6782 |
| net_avg_loss | -101.4970 |
| avg_hold_time_bars | 41.2326 |
| exposure | 0.5374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
