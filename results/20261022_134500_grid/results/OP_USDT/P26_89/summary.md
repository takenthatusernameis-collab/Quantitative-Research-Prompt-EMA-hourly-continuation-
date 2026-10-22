# EMA Hourly Continuation — OP/USDT P26_89

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.5742 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -4.2860 |
| sortino_ratio | -1.5958 |
| max_drawdown | 0.8529 |
| cagr | -0.5271 |
| net_avg_win | 35.3881 |
| net_avg_loss | -53.9446 |
| avg_hold_time_bars | 10.1156 |
| exposure | 0.3182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
