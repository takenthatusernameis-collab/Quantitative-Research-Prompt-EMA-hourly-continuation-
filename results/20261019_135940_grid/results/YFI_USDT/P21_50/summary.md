# EMA Hourly Continuation — YFI/USDT P21_50

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1130 |
| net_profit_factor | 0.4389 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -10.3769 |
| sortino_ratio | -4.9325 |
| max_drawdown | 0.9983 |
| cagr | -0.9186 |
| net_avg_win | 16.2667 |
| net_avg_loss | -27.3694 |
| avg_hold_time_bars | 4.2425 |
| exposure | 0.2169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
