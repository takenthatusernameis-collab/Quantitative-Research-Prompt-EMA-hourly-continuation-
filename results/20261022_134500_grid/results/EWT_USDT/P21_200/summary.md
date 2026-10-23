# EMA Hourly Continuation — EWT/USDT P21_200

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5816 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.7986 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -3.8540 |
| sortino_ratio | -1.2223 |
| max_drawdown | 0.8015 |
| cagr | -0.4435 |
| net_avg_win | 47.1739 |
| net_avg_loss | -64.3818 |
| avg_hold_time_bars | 21.1481 |
| exposure | 0.4931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
