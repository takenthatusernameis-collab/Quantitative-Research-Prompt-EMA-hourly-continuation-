# EMA Hourly Continuation — MOG/USDT P34_50

**Symbol:** MOG/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.8208 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.1054 |
| sortino_ratio | -0.2560 |
| max_drawdown | 0.3448 |
| cagr | -0.1120 |
| net_avg_win | 90.3603 |
| net_avg_loss | -113.8570 |
| avg_hold_time_bars | 4.8109 |
| exposure | 0.0569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
