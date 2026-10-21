# EMA Hourly Continuation — BONK/USDT P20_89

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8284 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.2333 |
| sortino_ratio | -0.3703 |
| max_drawdown | 0.4351 |
| cagr | -0.1587 |
| net_avg_win | 77.5998 |
| net_avg_loss | -92.4103 |
| avg_hold_time_bars | 18.3152 |
| exposure | 0.3671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
