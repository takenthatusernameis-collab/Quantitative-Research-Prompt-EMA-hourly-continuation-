# EMA Hourly Continuation — CKB/USDT P100_200

**Symbol:** CKB/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -2.7320 |
| sortino_ratio | -0.7911 |
| max_drawdown | 0.6136 |
| cagr | -0.3130 |
| net_avg_win | 48.7443 |
| net_avg_loss | -79.6462 |
| avg_hold_time_bars | 8.9357 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
