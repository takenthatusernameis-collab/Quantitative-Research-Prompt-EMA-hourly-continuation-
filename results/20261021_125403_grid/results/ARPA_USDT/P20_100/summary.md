# EMA Hourly Continuation — ARPA/USDT P20_100

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9196 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.8722 |
| sortino_ratio | -0.9640 |
| max_drawdown | 0.7056 |
| cagr | -0.3572 |
| net_avg_win | 57.3873 |
| net_avg_loss | -75.3524 |
| avg_hold_time_bars | 16.1727 |
| exposure | 0.4069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
