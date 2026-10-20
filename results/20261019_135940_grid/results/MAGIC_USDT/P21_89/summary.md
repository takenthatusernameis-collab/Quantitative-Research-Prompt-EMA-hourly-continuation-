# EMA Hourly Continuation — MAGIC/USDT P21_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6930 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -3.2366 |
| sortino_ratio | -1.1659 |
| max_drawdown | 0.7606 |
| cagr | -0.4270 |
| net_avg_win | 52.6230 |
| net_avg_loss | -73.6558 |
| avg_hold_time_bars | 14.2957 |
| exposure | 0.4263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
