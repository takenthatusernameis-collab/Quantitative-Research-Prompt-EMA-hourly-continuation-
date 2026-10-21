# EMA Hourly Continuation — POL/USDT P21_34

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.5929 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8471 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -3.0004 |
| sortino_ratio | -0.7522 |
| max_drawdown | 0.6046 |
| cagr | -0.2920 |
| net_avg_win | 60.7510 |
| net_avg_loss | -84.2802 |
| avg_hold_time_bars | 5.7273 |
| exposure | 0.0802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
