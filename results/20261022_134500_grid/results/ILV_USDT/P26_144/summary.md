# EMA Hourly Continuation — ILV/USDT P26_144

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6676 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.7035 |
| sortino_ratio | -0.8622 |
| max_drawdown | 0.6532 |
| cagr | -0.3367 |
| net_avg_win | 51.4907 |
| net_avg_loss | -74.7419 |
| avg_hold_time_bars | 20.2510 |
| exposure | 0.4695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
