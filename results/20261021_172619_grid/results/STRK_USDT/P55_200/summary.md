# EMA Hourly Continuation — STRK/USDT P55_200

**Symbol:** STRK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.9400 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1135 |
| gross_win_rate | 0.5298 |
| sharpe_ratio | -0.2680 |
| sortino_ratio | -0.0653 |
| max_drawdown | 0.1973 |
| cagr | -0.0337 |
| net_avg_win | 85.5527 |
| net_avg_loss | -102.5566 |
| avg_hold_time_bars | 27.9228 |
| exposure | 0.3617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
