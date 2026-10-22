# EMA Hourly Continuation — SQD/USDT P12_26

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.7692 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -1.8309 |
| sortino_ratio | -0.5683 |
| max_drawdown | 0.4893 |
| cagr | -0.2308 |
| net_avg_win | 69.7828 |
| net_avg_loss | -88.3698 |
| avg_hold_time_bars | 5.7193 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
