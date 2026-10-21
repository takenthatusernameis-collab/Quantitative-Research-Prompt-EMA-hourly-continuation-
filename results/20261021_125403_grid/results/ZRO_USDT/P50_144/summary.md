# EMA Hourly Continuation — ZRO/USDT P50_144

**Symbol:** ZRO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.8674 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0320 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -0.8271 |
| sortino_ratio | -0.2192 |
| max_drawdown | 0.3168 |
| cagr | -0.0985 |
| net_avg_win | 87.3063 |
| net_avg_loss | -103.8747 |
| avg_hold_time_bars | 14.9874 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
