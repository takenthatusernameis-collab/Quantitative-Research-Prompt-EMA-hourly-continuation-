# EMA Hourly Continuation — STRK/USDT P20_21

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 124 |
| net_profit_factor | 0.6586 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8742 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -1.4389 |
| sortino_ratio | -0.2287 |
| max_drawdown | 0.2523 |
| cagr | -0.0997 |
| net_avg_win | 77.0861 |
| net_avg_loss | -102.8614 |
| avg_hold_time_bars | 5.0968 |
| exposure | 0.0287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
