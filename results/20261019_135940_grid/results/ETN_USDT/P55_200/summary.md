# EMA Hourly Continuation — ETN/USDT P55_200

**Symbol:** ETN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.4794 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.6846 |
| gross_win_rate | 0.3995 |
| sharpe_ratio | -5.8471 |
| sortino_ratio | -1.8742 |
| max_drawdown | 0.8599 |
| cagr | -0.5986 |
| net_avg_win | 45.6783 |
| net_avg_loss | -61.6094 |
| avg_hold_time_bars | 13.2397 |
| exposure | 0.3150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
