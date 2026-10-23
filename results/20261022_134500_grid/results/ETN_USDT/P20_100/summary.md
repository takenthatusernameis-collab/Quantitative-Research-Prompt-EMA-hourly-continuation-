# EMA Hourly Continuation — ETN/USDT P20_100

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.4209 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.6318 |
| gross_win_rate | 0.3899 |
| sharpe_ratio | -8.2889 |
| sortino_ratio | -3.3547 |
| max_drawdown | 0.9685 |
| cagr | -0.8062 |
| net_avg_win | 26.8627 |
| net_avg_loss | -38.6146 |
| avg_hold_time_bars | 10.0777 |
| exposure | 0.3804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
