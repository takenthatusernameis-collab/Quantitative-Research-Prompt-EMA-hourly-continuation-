# EMA Hourly Continuation — CFX/USDT P26_89

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6251 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9891 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -3.6745 |
| sortino_ratio | -1.3210 |
| max_drawdown | 0.7992 |
| cagr | -0.4676 |
| net_avg_win | 41.4090 |
| net_avg_loss | -64.0392 |
| avg_hold_time_bars | 11.3456 |
| exposure | 0.3357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
