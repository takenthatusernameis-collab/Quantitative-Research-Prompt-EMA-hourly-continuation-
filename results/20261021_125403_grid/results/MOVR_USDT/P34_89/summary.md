# EMA Hourly Continuation — MOVR/USDT P34_89

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6799 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8762 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -2.6855 |
| sortino_ratio | -0.8298 |
| max_drawdown | 0.6550 |
| cagr | -0.3177 |
| net_avg_win | 59.8515 |
| net_avg_loss | -76.5015 |
| avg_hold_time_bars | 10.1019 |
| exposure | 0.2163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
