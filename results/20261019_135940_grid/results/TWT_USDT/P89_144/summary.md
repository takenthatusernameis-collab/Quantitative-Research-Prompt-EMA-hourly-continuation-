# EMA Hourly Continuation — TWT/USDT P89_144

**Symbol:** TWT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.3508 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.7576 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -6.5912 |
| sortino_ratio | -2.0920 |
| max_drawdown | 0.9282 |
| cagr | -0.6451 |
| net_avg_win | 23.9407 |
| net_avg_loss | -48.8430 |
| avg_hold_time_bars | 5.7485 |
| exposure | 0.1309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
