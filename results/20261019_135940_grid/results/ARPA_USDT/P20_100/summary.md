# EMA Hourly Continuation — ARPA/USDT P20_100

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.6036 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.9278 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -5.1869 |
| sortino_ratio | -1.9770 |
| max_drawdown | 0.9155 |
| cagr | -0.6133 |
| net_avg_win | 41.0705 |
| net_avg_loss | -57.0409 |
| avg_hold_time_bars | 12.7118 |
| exposure | 0.4251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
