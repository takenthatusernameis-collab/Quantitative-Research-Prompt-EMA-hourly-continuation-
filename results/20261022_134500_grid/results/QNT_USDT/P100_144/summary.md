# EMA Hourly Continuation — QNT/USDT P100_144

**Symbol:** QNT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.3661 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.7526 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -6.7072 |
| sortino_ratio | -2.2987 |
| max_drawdown | 0.9363 |
| cagr | -0.6650 |
| net_avg_win | 22.0584 |
| net_avg_loss | -45.5637 |
| avg_hold_time_bars | 3.7909 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
