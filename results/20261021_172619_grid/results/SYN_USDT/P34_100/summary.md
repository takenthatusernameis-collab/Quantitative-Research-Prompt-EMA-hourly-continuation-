# EMA Hourly Continuation — SYN/USDT P34_100

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.8505 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0513 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.1434 |
| sortino_ratio | -0.3453 |
| max_drawdown | 0.3954 |
| cagr | -0.1493 |
| net_avg_win | 84.0302 |
| net_avg_loss | -102.8975 |
| avg_hold_time_bars | 14.1129 |
| exposure | 0.2842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
