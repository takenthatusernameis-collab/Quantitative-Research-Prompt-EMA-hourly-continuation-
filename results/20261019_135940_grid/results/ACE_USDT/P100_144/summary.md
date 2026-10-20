# EMA Hourly Continuation — ACE/USDT P100_144

**Symbol:** ACE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.5011 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8597 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -4.1462 |
| sortino_ratio | -1.2011 |
| max_drawdown | 0.7628 |
| cagr | -0.4347 |
| net_avg_win | 40.3178 |
| net_avg_loss | -66.7617 |
| avg_hold_time_bars | 5.7637 |
| exposure | 0.1093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
