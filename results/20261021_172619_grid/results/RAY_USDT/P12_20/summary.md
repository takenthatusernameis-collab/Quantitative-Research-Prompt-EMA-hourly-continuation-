# EMA Hourly Continuation — RAY/USDT P12_20

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7264 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0210 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.8980 |
| sortino_ratio | -0.5013 |
| max_drawdown | 0.5075 |
| cagr | -0.2066 |
| net_avg_win | 68.4252 |
| net_avg_loss | -95.8836 |
| avg_hold_time_bars | 4.5693 |
| exposure | 0.0704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
