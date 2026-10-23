# EMA Hourly Continuation — PROM/USDT P50_89

**Symbol:** PROM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.4363 |
| net_win_rate | 0.4040 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -7.8154 |
| sortino_ratio | -3.0167 |
| max_drawdown | 0.9767 |
| cagr | -0.7742 |
| net_avg_win | 25.1048 |
| net_avg_loss | -39.0049 |
| avg_hold_time_bars | 5.0819 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
