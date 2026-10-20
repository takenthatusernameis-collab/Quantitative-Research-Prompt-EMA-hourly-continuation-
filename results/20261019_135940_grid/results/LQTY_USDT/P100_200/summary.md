# EMA Hourly Continuation — LQTY/USDT P100_200

**Symbol:** LQTY/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.6520 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9584 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.5422 |
| sortino_ratio | -0.7152 |
| max_drawdown | 0.5677 |
| cagr | -0.2815 |
| net_avg_win | 56.0651 |
| net_avg_loss | -79.6690 |
| avg_hold_time_bars | 9.3079 |
| exposure | 0.1655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
