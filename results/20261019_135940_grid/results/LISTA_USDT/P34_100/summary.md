# EMA Hourly Continuation — LISTA/USDT P34_100

**Symbol:** LISTA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.5789 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8589 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -4.1369 |
| sortino_ratio | -1.4378 |
| max_drawdown | 0.7982 |
| cagr | -0.4941 |
| net_avg_win | 42.2641 |
| net_avg_loss | -61.3914 |
| avg_hold_time_bars | 10.9171 |
| exposure | 0.3027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
