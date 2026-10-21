# EMA Hourly Continuation — AIOZ/USDT P20_34

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4281 |
| gross_profit_factor | 0.7587 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -3.1510 |
| sortino_ratio | -0.7913 |
| max_drawdown | 0.6309 |
| cagr | -0.3055 |
| net_avg_win | 61.5490 |
| net_avg_loss | -79.5751 |
| avg_hold_time_bars | 5.6869 |
| exposure | 0.0809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
