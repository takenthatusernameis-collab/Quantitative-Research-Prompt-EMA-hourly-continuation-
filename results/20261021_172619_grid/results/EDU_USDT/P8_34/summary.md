# EMA Hourly Continuation — EDU/USDT P8_34

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.7938 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.1804 |
| sortino_ratio | -0.8934 |
| max_drawdown | 0.6591 |
| cagr | -0.3374 |
| net_avg_win | 60.2151 |
| net_avg_loss | -76.9747 |
| avg_hold_time_bars | 8.7707 |
| exposure | 0.3254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
