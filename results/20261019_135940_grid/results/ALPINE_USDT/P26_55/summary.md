# EMA Hourly Continuation — ALPINE/USDT P26_55

**Symbol:** ALPINE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.4479 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.8171 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -7.6723 |
| sortino_ratio | -3.1783 |
| max_drawdown | 0.9801 |
| cagr | -0.7876 |
| net_avg_win | 21.8954 |
| net_avg_loss | -36.2116 |
| avg_hold_time_bars | 5.9906 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
