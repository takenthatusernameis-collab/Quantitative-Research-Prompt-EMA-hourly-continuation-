# EMA Hourly Continuation — SKL/USDT P50_100

**Symbol:** SKL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6960 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.2033 |
| sortino_ratio | -0.6224 |
| max_drawdown | 0.5336 |
| cagr | -0.2482 |
| net_avg_win | 62.3126 |
| net_avg_loss | -82.5033 |
| avg_hold_time_bars | 9.1276 |
| exposure | 0.1626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
