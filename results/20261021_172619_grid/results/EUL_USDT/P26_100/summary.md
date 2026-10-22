# EMA Hourly Continuation — EUL/USDT P26_100

**Symbol:** EUL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7228 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8874 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.0064 |
| sortino_ratio | -0.5848 |
| max_drawdown | 0.5095 |
| cagr | -0.2355 |
| net_avg_win | 64.5921 |
| net_avg_loss | -80.0626 |
| avg_hold_time_bars | 16.6086 |
| exposure | 0.3163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
