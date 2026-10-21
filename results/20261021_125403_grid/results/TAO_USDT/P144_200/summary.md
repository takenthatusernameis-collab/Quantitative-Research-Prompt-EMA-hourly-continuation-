# EMA Hourly Continuation — TAO/USDT P144_200

**Symbol:** TAO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.6106 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.7804 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -1.9256 |
| sortino_ratio | -0.3702 |
| max_drawdown | 0.3475 |
| cagr | -0.1564 |
| net_avg_win | 66.4462 |
| net_avg_loss | -88.3555 |
| avg_hold_time_bars | 7.3552 |
| exposure | 0.0612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
