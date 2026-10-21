# EMA Hourly Continuation — CPOOL/USDT P26_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7156 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.8897 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.8488 |
| sortino_ratio | -0.5212 |
| max_drawdown | 0.4730 |
| cagr | -0.2132 |
| net_avg_win | 60.5330 |
| net_avg_loss | -78.7296 |
| avg_hold_time_bars | 6.4615 |
| exposure | 0.1145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
