# EMA Hourly Continuation — SUI/USDT P26_100

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6398 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -4.2187 |
| sortino_ratio | -1.5414 |
| max_drawdown | 0.8622 |
| cagr | -0.5313 |
| net_avg_win | 46.3725 |
| net_avg_loss | -66.1810 |
| avg_hold_time_bars | 10.8638 |
| exposure | 0.3373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
