# EMA Hourly Continuation — CHR/USDT P8_89

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.7883 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9510 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -1.9509 |
| sortino_ratio | -0.6464 |
| max_drawdown | 0.5689 |
| cagr | -0.2587 |
| net_avg_win | 75.6371 |
| net_avg_loss | -88.8007 |
| avg_hold_time_bars | 26.0147 |
| exposure | 0.6392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
