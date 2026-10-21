# EMA Hourly Continuation — ARB/USDT P144_200

**Symbol:** ARB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.7393 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0037 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.2132 |
| sortino_ratio | -0.2292 |
| max_drawdown | 0.2462 |
| cagr | -0.1001 |
| net_avg_win | 75.8703 |
| net_avg_loss | -103.8114 |
| avg_hold_time_bars | 7.4277 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
