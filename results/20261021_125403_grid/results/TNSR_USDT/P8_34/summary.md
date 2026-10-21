# EMA Hourly Continuation — TNSR/USDT P8_34

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.8395 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0693 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.8412 |
| sortino_ratio | -0.7166 |
| max_drawdown | 0.6202 |
| cagr | -0.2826 |
| net_avg_win | 78.7080 |
| net_avg_loss | -97.6405 |
| avg_hold_time_bars | 9.3586 |
| exposure | 0.3130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
