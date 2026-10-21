# EMA Hourly Continuation — IMX/USDT P50_144

**Symbol:** IMX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7511 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9216 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.4104 |
| sortino_ratio | -0.3784 |
| max_drawdown | 0.4228 |
| cagr | -0.1605 |
| net_avg_win | 61.8982 |
| net_avg_loss | -79.6594 |
| avg_hold_time_bars | 16.2288 |
| exposure | 0.2600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
