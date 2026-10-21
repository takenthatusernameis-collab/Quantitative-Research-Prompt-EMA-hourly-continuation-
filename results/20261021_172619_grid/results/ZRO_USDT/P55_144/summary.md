# EMA Hourly Continuation — ZRO/USDT P55_144

**Symbol:** ZRO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.9680 |
| net_win_rate | 0.5390 |
| gross_profit_factor | 1.1580 |
| gross_win_rate | 0.5390 |
| sharpe_ratio | -0.1328 |
| sortino_ratio | -0.0350 |
| max_drawdown | 0.1962 |
| cagr | -0.0217 |
| net_avg_win | 90.7099 |
| net_avg_loss | -109.5491 |
| avg_hold_time_bars | 13.5844 |
| exposure | 0.2048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
