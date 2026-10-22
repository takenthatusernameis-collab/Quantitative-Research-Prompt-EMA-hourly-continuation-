# EMA Hourly Continuation — XAI/USDT P12_20

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6469 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8779 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -2.6788 |
| sortino_ratio | -0.7463 |
| max_drawdown | 0.6041 |
| cagr | -0.2893 |
| net_avg_win | 58.9415 |
| net_avg_loss | -81.1408 |
| avg_hold_time_bars | 4.7079 |
| exposure | 0.0813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
