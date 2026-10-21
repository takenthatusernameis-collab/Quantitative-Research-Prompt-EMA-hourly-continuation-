# EMA Hourly Continuation — SUSHI/USDT P8_34

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.7070 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9249 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.0665 |
| sortino_ratio | -1.1770 |
| max_drawdown | 0.7527 |
| cagr | -0.4175 |
| net_avg_win | 51.6056 |
| net_avg_loss | -67.1961 |
| avg_hold_time_bars | 9.2989 |
| exposure | 0.3055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
