# EMA Hourly Continuation — WIN/USDT P34_144

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.4897 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -4.8526 |
| sortino_ratio | -1.4772 |
| max_drawdown | 0.8389 |
| cagr | -0.5127 |
| net_avg_win | 38.9192 |
| net_avg_loss | -63.4607 |
| avg_hold_time_bars | 18.6379 |
| exposure | 0.3931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
