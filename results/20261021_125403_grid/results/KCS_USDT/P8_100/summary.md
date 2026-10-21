# EMA Hourly Continuation — KCS/USDT P8_100

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5234 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8019 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -4.5462 |
| sortino_ratio | -1.4186 |
| max_drawdown | 0.8229 |
| cagr | -0.4842 |
| net_avg_win | 42.3772 |
| net_avg_loss | -63.2066 |
| avg_hold_time_bars | 29.1357 |
| exposure | 0.6344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
