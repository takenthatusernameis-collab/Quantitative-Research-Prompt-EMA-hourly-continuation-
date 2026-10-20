# EMA Hourly Continuation — EDU/USDT P26_100

**Symbol:** EDU/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.5626 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -4.3303 |
| sortino_ratio | -1.6304 |
| max_drawdown | 0.8646 |
| cagr | -0.5386 |
| net_avg_win | 33.6410 |
| net_avg_loss | -50.5492 |
| avg_hold_time_bars | 11.1816 |
| exposure | 0.3623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
