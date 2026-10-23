# EMA Hourly Continuation — XCH/USDT P26_200

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.5743 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8513 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -3.4038 |
| sortino_ratio | -1.0463 |
| max_drawdown | 0.7252 |
| cagr | -0.3995 |
| net_avg_win | 43.3097 |
| net_avg_loss | -65.0068 |
| avg_hold_time_bars | 26.0432 |
| exposure | 0.5753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
