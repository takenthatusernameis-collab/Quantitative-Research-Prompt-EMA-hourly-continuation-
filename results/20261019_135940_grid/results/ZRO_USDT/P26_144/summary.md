# EMA Hourly Continuation — ZRO/USDT P26_144

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6848 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8953 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -2.8247 |
| sortino_ratio | -0.9049 |
| max_drawdown | 0.6436 |
| cagr | -0.3447 |
| net_avg_win | 61.0581 |
| net_avg_loss | -78.9054 |
| avg_hold_time_bars | 20.6189 |
| exposure | 0.4794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
