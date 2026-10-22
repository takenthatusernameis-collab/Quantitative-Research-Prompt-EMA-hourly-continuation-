# EMA Hourly Continuation — UNI/USDT P26_100

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5978 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -4.0391 |
| sortino_ratio | -1.4253 |
| max_drawdown | 0.8293 |
| cagr | -0.4999 |
| net_avg_win | 40.3093 |
| net_avg_loss | -61.5588 |
| avg_hold_time_bars | 11.5338 |
| exposure | 0.3340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
