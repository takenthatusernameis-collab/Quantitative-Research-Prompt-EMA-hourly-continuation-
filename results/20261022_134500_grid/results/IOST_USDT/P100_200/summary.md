# EMA Hourly Continuation — IOST/USDT P100_200

**Symbol:** IOST/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5539 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 1.0043 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -3.5211 |
| sortino_ratio | -1.0007 |
| max_drawdown | 0.7154 |
| cagr | -0.3859 |
| net_avg_win | 45.1993 |
| net_avg_loss | -74.6669 |
| avg_hold_time_bars | 9.3227 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
