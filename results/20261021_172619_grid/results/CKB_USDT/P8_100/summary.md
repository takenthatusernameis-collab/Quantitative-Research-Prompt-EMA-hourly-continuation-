# EMA Hourly Continuation — CKB/USDT P8_100

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.8257 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0030 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.3037 |
| sortino_ratio | -0.3998 |
| max_drawdown | 0.3823 |
| cagr | -0.1699 |
| net_avg_win | 76.9357 |
| net_avg_loss | -93.5782 |
| avg_hold_time_bars | 32.9020 |
| exposure | 0.6865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
