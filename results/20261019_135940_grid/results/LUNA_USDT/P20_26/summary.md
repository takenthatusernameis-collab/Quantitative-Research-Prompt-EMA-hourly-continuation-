# EMA Hourly Continuation — LUNA/USDT P20_26

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1305 |
| net_profit_factor | 0.2400 |
| net_win_rate | 0.3402 |
| gross_profit_factor | 0.7956 |
| gross_win_rate | 0.3977 |
| sharpe_ratio | -16.2905 |
| sortino_ratio | -8.6425 |
| max_drawdown | 1.0000 |
| cagr | -0.9912 |
| net_avg_win | 7.1111 |
| net_avg_loss | -15.2814 |
| avg_hold_time_bars | 1.8452 |
| exposure | 0.1095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
