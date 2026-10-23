# EMA Hourly Continuation — BRETT/USDT P55_89

**Symbol:** BRETT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -4.5281 |
| sortino_ratio | -1.6653 |
| max_drawdown | 0.8536 |
| cagr | -0.5500 |
| net_avg_win | 43.3095 |
| net_avg_loss | -63.8989 |
| avg_hold_time_bars | 3.7963 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
