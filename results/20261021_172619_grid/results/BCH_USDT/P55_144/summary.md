# EMA Hourly Continuation — BCH/USDT P55_144

**Symbol:** BCH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.7198 |
| sortino_ratio | -0.4379 |
| max_drawdown | 0.4477 |
| cagr | -0.1822 |
| net_avg_win | 74.1831 |
| net_avg_loss | -97.1106 |
| avg_hold_time_bars | 16.1108 |
| exposure | 0.2314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
