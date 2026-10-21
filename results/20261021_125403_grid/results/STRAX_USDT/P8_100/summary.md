# EMA Hourly Continuation — STRAX/USDT P8_100

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -3.1544 |
| sortino_ratio | -1.1072 |
| max_drawdown | 0.7396 |
| cagr | -0.3996 |
| net_avg_win | 62.1211 |
| net_avg_loss | -75.2187 |
| avg_hold_time_bars | 21.2702 |
| exposure | 0.5903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
