# EMA Hourly Continuation — CPOOL/USDT P12_20

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1470 |
| net_profit_factor | 0.4727 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -11.9641 |
| sortino_ratio | -6.4573 |
| max_drawdown | 0.9998 |
| cagr | -0.9633 |
| net_avg_win | 14.9865 |
| net_avg_loss | -21.7425 |
| avg_hold_time_bars | 2.2925 |
| exposure | 0.1532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
