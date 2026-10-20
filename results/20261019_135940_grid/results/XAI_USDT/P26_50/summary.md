# EMA Hourly Continuation — XAI/USDT P26_50

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.5682 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -7.1238 |
| sortino_ratio | -3.1894 |
| max_drawdown | 0.9807 |
| cagr | -0.7871 |
| net_avg_win | 28.5178 |
| net_avg_loss | -40.5807 |
| avg_hold_time_bars | 4.1306 |
| exposure | 0.1898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
