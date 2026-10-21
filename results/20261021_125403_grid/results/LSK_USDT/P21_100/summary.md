# EMA Hourly Continuation — LSK/USDT P21_100

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7004 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9175 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -2.5560 |
| sortino_ratio | -0.8055 |
| max_drawdown | 0.6299 |
| cagr | -0.3113 |
| net_avg_win | 61.2853 |
| net_avg_loss | -78.6775 |
| avg_hold_time_bars | 18.0490 |
| exposure | 0.4020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
