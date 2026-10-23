# EMA Hourly Continuation — SUSHI/USDT P50_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6540 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.4837 |
| sortino_ratio | -0.7124 |
| max_drawdown | 0.5964 |
| cagr | -0.2847 |
| net_avg_win | 53.6596 |
| net_avg_loss | -77.7902 |
| avg_hold_time_bars | 21.5981 |
| exposure | 0.4036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
