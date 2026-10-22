# EMA Hourly Continuation — BCH/USDT P100_144

**Symbol:** BCH/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.4504 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -5.5274 |
| sortino_ratio | -1.7352 |
| max_drawdown | 0.8826 |
| cagr | -0.5681 |
| net_avg_win | 33.0239 |
| net_avg_loss | -60.3215 |
| avg_hold_time_bars | 3.9731 |
| exposure | 0.0872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
