# EMA Hourly Continuation — WOO/USDT P21_100

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.7126 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 1.0342 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -3.3153 |
| sortino_ratio | -1.1581 |
| max_drawdown | 0.7778 |
| cagr | -0.4199 |
| net_avg_win | 63.9523 |
| net_avg_loss | -81.0482 |
| avg_hold_time_bars | 15.6092 |
| exposure | 0.4321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
