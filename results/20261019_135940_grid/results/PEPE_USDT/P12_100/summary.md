# EMA Hourly Continuation — PEPE/USDT P12_100

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6336 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -4.3688 |
| sortino_ratio | -1.5170 |
| max_drawdown | 0.8464 |
| cagr | -0.5208 |
| net_avg_win | 52.5914 |
| net_avg_loss | -68.4272 |
| avg_hold_time_bars | 21.0669 |
| exposure | 0.5870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
