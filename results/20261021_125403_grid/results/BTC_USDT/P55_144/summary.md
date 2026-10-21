# EMA Hourly Continuation — BTC/USDT P55_144

**Symbol:** BTC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7354 |
| net_win_rate | 0.5425 |
| gross_profit_factor | 1.2149 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | -1.7438 |
| sortino_ratio | -0.4380 |
| max_drawdown | 0.4779 |
| cagr | -0.1792 |
| net_avg_win | 64.7101 |
| net_avg_loss | -104.3549 |
| avg_hold_time_bars | 15.9501 |
| exposure | 0.2176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
