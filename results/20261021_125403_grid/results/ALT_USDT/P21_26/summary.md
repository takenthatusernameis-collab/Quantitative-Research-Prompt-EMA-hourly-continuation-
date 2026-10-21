# EMA Hourly Continuation — ALT/USDT P21_26

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -2.7977 |
| sortino_ratio | -0.7555 |
| max_drawdown | 0.5944 |
| cagr | -0.2929 |
| net_avg_win | 56.6014 |
| net_avg_loss | -82.2370 |
| avg_hold_time_bars | 5.4270 |
| exposure | 0.0878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
