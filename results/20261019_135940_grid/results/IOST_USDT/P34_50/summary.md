# EMA Hourly Continuation — IOST/USDT P34_50

**Symbol:** IOST/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.3260 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.8151 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -9.5773 |
| sortino_ratio | -4.1010 |
| max_drawdown | 0.9946 |
| cagr | -0.8730 |
| net_avg_win | 12.7577 |
| net_avg_loss | -28.4817 |
| avg_hold_time_bars | 3.1218 |
| exposure | 0.1270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
