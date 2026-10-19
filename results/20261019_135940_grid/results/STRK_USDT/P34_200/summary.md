# EMA Hourly Continuation — STRK/USDT P34_200

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8490 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.4982 |
| sortino_ratio | -0.6867 |
| max_drawdown | 0.5712 |
| cagr | -0.2738 |
| net_avg_win | 57.1902 |
| net_avg_loss | -76.9797 |
| avg_hold_time_bars | 28.4907 |
| exposure | 0.4856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
