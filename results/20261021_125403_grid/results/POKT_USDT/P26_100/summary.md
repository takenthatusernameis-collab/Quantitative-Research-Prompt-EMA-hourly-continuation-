# EMA Hourly Continuation — POKT/USDT P26_100

**Symbol:** POKT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7116 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -2.8096 |
| sortino_ratio | -0.8998 |
| max_drawdown | 0.6903 |
| cagr | -0.3405 |
| net_avg_win | 67.9678 |
| net_avg_loss | -81.3753 |
| avg_hold_time_bars | 14.3782 |
| exposure | 0.3338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
