# EMA Hourly Continuation — THETA/USDT P34_144

**Symbol:** THETA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.5951 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9066 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -3.5259 |
| sortino_ratio | -1.1421 |
| max_drawdown | 0.7516 |
| cagr | -0.4163 |
| net_avg_win | 44.2946 |
| net_avg_loss | -65.8603 |
| avg_hold_time_bars | 14.5534 |
| exposure | 0.3466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
