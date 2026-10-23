# EMA Hourly Continuation — CWEB/USDT P21_89

**Symbol:** CWEB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.4859 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.8193 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -6.6846 |
| sortino_ratio | -2.2408 |
| max_drawdown | 0.9457 |
| cagr | -0.6832 |
| net_avg_win | 38.7995 |
| net_avg_loss | -53.2353 |
| avg_hold_time_bars | 16.1026 |
| exposure | 0.4209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
