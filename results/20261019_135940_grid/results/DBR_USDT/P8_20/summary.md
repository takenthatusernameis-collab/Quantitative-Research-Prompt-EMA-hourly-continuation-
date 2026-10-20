# EMA Hourly Continuation — DBR/USDT P8_20

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.4755 |
| net_win_rate | 0.4276 |
| gross_profit_factor | 1.0561 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -10.5568 |
| sortino_ratio | -5.3542 |
| max_drawdown | 0.9957 |
| cagr | -0.9335 |
| net_avg_win | 20.5139 |
| net_avg_loss | -32.2287 |
| avg_hold_time_bars | 4.3605 |
| exposure | 0.2552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
