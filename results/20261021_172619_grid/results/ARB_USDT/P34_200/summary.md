# EMA Hourly Continuation — ARB/USDT P34_200

**Symbol:** ARB/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 1.0599 |
| net_win_rate | 0.5564 |
| gross_profit_factor | 1.2364 |
| gross_win_rate | 0.5564 |
| sharpe_ratio | 0.3616 |
| sortino_ratio | 0.0844 |
| max_drawdown | 0.1445 |
| cagr | 0.0319 |
| net_avg_win | 101.3338 |
| net_avg_loss | -119.9236 |
| avg_hold_time_bars | 46.3619 |
| exposure | 0.5416 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
