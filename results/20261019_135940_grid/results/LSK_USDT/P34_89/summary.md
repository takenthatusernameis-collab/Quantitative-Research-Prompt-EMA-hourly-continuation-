# EMA Hourly Continuation — LSK/USDT P34_89

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5422 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.9010 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -5.1370 |
| sortino_ratio | -1.8286 |
| max_drawdown | 0.8981 |
| cagr | -0.5851 |
| net_avg_win | 37.1178 |
| net_avg_loss | -55.0814 |
| avg_hold_time_bars | 8.6892 |
| exposure | 0.2516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
