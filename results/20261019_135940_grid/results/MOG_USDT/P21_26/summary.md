# EMA Hourly Continuation — MOG/USDT P21_26

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1080 |
| net_profit_factor | 0.4478 |
| net_win_rate | 0.4074 |
| gross_profit_factor | 0.7988 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -11.1727 |
| sortino_ratio | -5.4386 |
| max_drawdown | 0.9984 |
| cagr | -0.9401 |
| net_avg_win | 18.3998 |
| net_avg_loss | -28.2505 |
| avg_hold_time_bars | 2.1074 |
| exposure | 0.1131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
