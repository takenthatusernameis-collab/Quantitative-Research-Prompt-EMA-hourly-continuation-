# EMA Hourly Continuation — IOTX/USDT P55_89

**Symbol:** IOTX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.6475 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9124 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.4784 |
| sortino_ratio | -0.6398 |
| max_drawdown | 0.5205 |
| cagr | -0.2537 |
| net_avg_win | 61.6889 |
| net_avg_loss | -86.8605 |
| avg_hold_time_bars | 6.6123 |
| exposure | 0.0977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
