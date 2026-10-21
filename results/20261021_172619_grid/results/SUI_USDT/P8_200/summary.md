# EMA Hourly Continuation — SUI/USDT P8_200

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.9029 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0503 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -0.5049 |
| sortino_ratio | -0.1255 |
| max_drawdown | 0.1998 |
| cagr | -0.0593 |
| net_avg_win | 85.8958 |
| net_avg_loss | -100.3486 |
| avg_hold_time_bars | 55.4733 |
| exposure | 0.7565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
