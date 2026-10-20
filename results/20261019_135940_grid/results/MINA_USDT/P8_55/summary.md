# EMA Hourly Continuation — MINA/USDT P8_55

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9803 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -4.8910 |
| sortino_ratio | -2.1181 |
| max_drawdown | 0.9330 |
| cagr | -0.6395 |
| net_avg_win | 33.3499 |
| net_avg_loss | -49.4655 |
| avg_hold_time_bars | 12.3716 |
| exposure | 0.5342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
