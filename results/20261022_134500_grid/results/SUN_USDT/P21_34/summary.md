# EMA Hourly Continuation — SUN/USDT P21_34

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.1230 |
| net_win_rate | 0.3100 |
| gross_profit_factor | 0.6001 |
| gross_win_rate | 0.4050 |
| sharpe_ratio | -15.2727 |
| sortino_ratio | -7.2790 |
| max_drawdown | 0.9999 |
| cagr | -0.9800 |
| net_avg_win | 4.5237 |
| net_avg_loss | -16.5244 |
| avg_hold_time_bars | 3.9790 |
| exposure | 0.1801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
