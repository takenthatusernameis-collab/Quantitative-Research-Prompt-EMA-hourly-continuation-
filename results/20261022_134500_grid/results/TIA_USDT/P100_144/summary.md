# EMA Hourly Continuation — TIA/USDT P100_144

**Symbol:** TIA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.5413 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -4.1288 |
| sortino_ratio | -1.2295 |
| max_drawdown | 0.7842 |
| cagr | -0.4457 |
| net_avg_win | 44.2779 |
| net_avg_loss | -71.6990 |
| avg_hold_time_bars | 3.9909 |
| exposure | 0.0800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
