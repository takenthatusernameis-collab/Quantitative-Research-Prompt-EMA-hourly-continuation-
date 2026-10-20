# EMA Hourly Continuation — WAVES/USDT P26_50

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.3558 |
| net_win_rate | 0.3865 |
| gross_profit_factor | 0.8452 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -11.5941 |
| sortino_ratio | -5.4354 |
| max_drawdown | 0.9991 |
| cagr | -0.9383 |
| net_avg_win | 13.2326 |
| net_avg_loss | -23.4273 |
| avg_hold_time_bars | 3.4764 |
| exposure | 0.1705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
