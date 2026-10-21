# EMA Hourly Continuation — XLM/USDT P34_100

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7597 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0586 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.5952 |
| sortino_ratio | -0.4537 |
| max_drawdown | 0.4253 |
| cagr | -0.1870 |
| net_avg_win | 63.7777 |
| net_avg_loss | -89.2766 |
| avg_hold_time_bars | 15.3487 |
| exposure | 0.2721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
