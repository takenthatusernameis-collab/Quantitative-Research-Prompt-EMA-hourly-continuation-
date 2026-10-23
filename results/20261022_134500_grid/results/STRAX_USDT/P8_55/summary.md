# EMA Hourly Continuation — STRAX/USDT P8_55

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.5935 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.9405 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -7.3149 |
| sortino_ratio | -3.3605 |
| max_drawdown | 0.9840 |
| cagr | -0.8093 |
| net_avg_win | 30.1796 |
| net_avg_loss | -40.4103 |
| avg_hold_time_bars | 9.8009 |
| exposure | 0.4817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
