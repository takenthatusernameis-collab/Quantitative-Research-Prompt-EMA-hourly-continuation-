# EMA Hourly Continuation — MOVR/USDT P8_144

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7994 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -1.3818 |
| sortino_ratio | -0.3994 |
| max_drawdown | 0.4166 |
| cagr | -0.1697 |
| net_avg_win | 73.9897 |
| net_avg_loss | -89.0093 |
| avg_hold_time_bars | 39.0195 |
| exposure | 0.7272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
