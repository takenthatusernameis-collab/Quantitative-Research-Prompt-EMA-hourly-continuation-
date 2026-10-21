# EMA Hourly Continuation — ETH/USDT P26_144

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.5875 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.7886 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -2.5293 |
| sortino_ratio | -0.5953 |
| max_drawdown | 0.5198 |
| cagr | -0.2396 |
| net_avg_win | 57.5896 |
| net_avg_loss | -79.8436 |
| avg_hold_time_bars | 41.5073 |
| exposure | 0.5170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
