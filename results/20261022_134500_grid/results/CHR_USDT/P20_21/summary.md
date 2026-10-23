# EMA Hourly Continuation — CHR/USDT P20_21

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.1122 |
| net_win_rate | 0.3119 |
| gross_profit_factor | 0.4945 |
| gross_win_rate | 0.3924 |
| sharpe_ratio | -16.0770 |
| sortino_ratio | -8.1612 |
| max_drawdown | 1.0000 |
| cagr | -0.9880 |
| net_avg_win | 3.4342 |
| net_avg_loss | -13.8715 |
| avg_hold_time_bars | 2.2602 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
