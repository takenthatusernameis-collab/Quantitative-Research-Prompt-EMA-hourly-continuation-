# EMA Hourly Continuation — CKB/USDT P26_89

**Symbol:** CKB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.5960 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -5.4517 |
| sortino_ratio | -2.0907 |
| max_drawdown | 0.9238 |
| cagr | -0.6363 |
| net_avg_win | 40.5674 |
| net_avg_loss | -56.0232 |
| avg_hold_time_bars | 9.2803 |
| exposure | 0.3130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
