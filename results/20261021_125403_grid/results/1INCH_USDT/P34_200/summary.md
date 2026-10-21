# EMA Hourly Continuation — 1INCH/USDT P34_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.8864 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.1023 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -0.5067 |
| sortino_ratio | -0.1107 |
| max_drawdown | 0.1741 |
| cagr | -0.0517 |
| net_avg_win | 80.4939 |
| net_avg_loss | -100.8044 |
| avg_hold_time_bars | 61.4826 |
| exposure | 0.6428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
