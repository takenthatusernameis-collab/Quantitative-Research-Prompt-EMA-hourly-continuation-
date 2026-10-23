# EMA Hourly Continuation — TRB/USDT P55_144

**Symbol:** TRB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.5490 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -4.1833 |
| sortino_ratio | -1.3597 |
| max_drawdown | 0.8069 |
| cagr | -0.4744 |
| net_avg_win | 39.8842 |
| net_avg_loss | -62.0129 |
| avg_hold_time_bars | 10.5414 |
| exposure | 0.2538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
