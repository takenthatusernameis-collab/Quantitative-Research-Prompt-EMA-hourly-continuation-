# EMA Hourly Continuation — SHR/USDT P34_200

**Symbol:** SHR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.5422 |
| net_win_rate | 0.3904 |
| gross_profit_factor | 0.6773 |
| gross_win_rate | 0.3904 |
| sharpe_ratio | -5.2436 |
| sortino_ratio | -1.8596 |
| max_drawdown | 0.8971 |
| cagr | -0.5828 |
| net_avg_win | 41.9808 |
| net_avg_loss | -49.5788 |
| avg_hold_time_bars | 14.9611 |
| exposure | 0.4353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
