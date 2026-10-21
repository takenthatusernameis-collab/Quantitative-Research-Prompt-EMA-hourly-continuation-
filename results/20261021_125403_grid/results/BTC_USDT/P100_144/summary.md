# EMA Hourly Continuation — BTC/USDT P100_144

**Symbol:** BTC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.6415 |
| net_win_rate | 0.5467 |
| gross_profit_factor | 1.2352 |
| gross_win_rate | 0.5556 |
| sharpe_ratio | -1.8317 |
| sortino_ratio | -0.3755 |
| max_drawdown | 0.4360 |
| cagr | -0.1549 |
| net_avg_win | 55.4843 |
| net_avg_loss | -104.2948 |
| avg_hold_time_bars | 7.0356 |
| exposure | 0.0633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
