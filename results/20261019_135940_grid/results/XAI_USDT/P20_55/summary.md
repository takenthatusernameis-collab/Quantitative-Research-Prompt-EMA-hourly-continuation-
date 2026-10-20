# EMA Hourly Continuation — XAI/USDT P20_55

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.6499 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -6.2854 |
| sortino_ratio | -2.8541 |
| max_drawdown | 0.9700 |
| cagr | -0.7465 |
| net_avg_win | 37.8319 |
| net_avg_loss | -48.6825 |
| avg_hold_time_bars | 5.7248 |
| exposure | 0.2714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
