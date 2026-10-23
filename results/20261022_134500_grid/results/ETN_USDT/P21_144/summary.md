# EMA Hourly Continuation — ETN/USDT P21_144

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.4329 |
| net_win_rate | 0.3695 |
| gross_profit_factor | 0.6295 |
| gross_win_rate | 0.3800 |
| sharpe_ratio | -7.5493 |
| sortino_ratio | -2.7580 |
| max_drawdown | 0.9450 |
| cagr | -0.7430 |
| net_avg_win | 34.0926 |
| net_avg_loss | -46.1617 |
| avg_hold_time_bars | 14.5271 |
| exposure | 0.4506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
