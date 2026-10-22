# EMA Hourly Continuation — ELON/USDT P20_55

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6548 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8720 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -2.9703 |
| sortino_ratio | -0.9057 |
| max_drawdown | 0.6572 |
| cagr | -0.3399 |
| net_avg_win | 57.9354 |
| net_avg_loss | -76.5650 |
| avg_hold_time_bars | 8.9300 |
| exposure | 0.1855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
