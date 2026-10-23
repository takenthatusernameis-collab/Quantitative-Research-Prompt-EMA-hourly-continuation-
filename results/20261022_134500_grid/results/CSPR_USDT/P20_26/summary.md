# EMA Hourly Continuation — CSPR/USDT P20_26

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1449 |
| net_profit_factor | 0.1521 |
| net_win_rate | 0.3230 |
| gross_profit_factor | 0.6045 |
| gross_win_rate | 0.3637 |
| sharpe_ratio | -17.0854 |
| sortino_ratio | -9.4749 |
| max_drawdown | 1.0000 |
| cagr | -0.9940 |
| net_avg_win | 3.8322 |
| net_avg_loss | -12.0218 |
| avg_hold_time_bars | 1.9551 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
