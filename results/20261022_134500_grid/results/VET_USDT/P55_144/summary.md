# EMA Hourly Continuation — VET/USDT P55_144

**Symbol:** VET/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.5984 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9712 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -3.2244 |
| sortino_ratio | -1.0165 |
| max_drawdown | 0.7304 |
| cagr | -0.3877 |
| net_avg_win | 42.0423 |
| net_avg_loss | -70.2600 |
| avg_hold_time_bars | 10.6016 |
| exposure | 0.2419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
