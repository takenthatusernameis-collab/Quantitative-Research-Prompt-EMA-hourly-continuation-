# EMA Hourly Continuation — BSV/USDT P55_144

**Symbol:** BSV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.5223 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.6973 |
| gross_win_rate | 0.4133 |
| sharpe_ratio | -3.8327 |
| sortino_ratio | -1.0511 |
| max_drawdown | 0.7046 |
| cagr | -0.3846 |
| net_avg_win | 49.7044 |
| net_avg_loss | -67.0454 |
| avg_hold_time_bars | 15.5253 |
| exposure | 0.2646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
