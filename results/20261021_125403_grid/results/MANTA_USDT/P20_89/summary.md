# EMA Hourly Continuation — MANTA/USDT P20_89

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7876 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9667 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -1.5657 |
| sortino_ratio | -0.4793 |
| max_drawdown | 0.4288 |
| cagr | -0.1983 |
| net_avg_win | 69.8779 |
| net_avg_loss | -86.4305 |
| avg_hold_time_bars | 19.8450 |
| exposure | 0.4131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
