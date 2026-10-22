# EMA Hourly Continuation — ZKJ/USDT P12_200

**Symbol:** ZKJ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.2801 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.6806 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -4.2305 |
| sortino_ratio | -0.7938 |
| max_drawdown | 0.6729 |
| cagr | -0.3305 |
| net_avg_win | 36.3322 |
| net_avg_loss | -84.8015 |
| avg_hold_time_bars | 117.9709 |
| exposure | 0.9223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
