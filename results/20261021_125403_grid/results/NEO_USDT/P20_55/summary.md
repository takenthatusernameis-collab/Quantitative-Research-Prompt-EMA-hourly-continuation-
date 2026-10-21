# EMA Hourly Continuation — NEO/USDT P20_55

**Symbol:** NEO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.6172 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -3.7036 |
| sortino_ratio | -1.2372 |
| max_drawdown | 0.7616 |
| cagr | -0.4322 |
| net_avg_win | 48.7257 |
| net_avg_loss | -66.9459 |
| avg_hold_time_bars | 8.7733 |
| exposure | 0.2181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
