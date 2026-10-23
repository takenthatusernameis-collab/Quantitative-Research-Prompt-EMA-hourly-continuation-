# EMA Hourly Continuation — ZEN/USDT P21_55

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.5046 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -6.9391 |
| sortino_ratio | -3.0822 |
| max_drawdown | 0.9793 |
| cagr | -0.7839 |
| net_avg_win | 21.7181 |
| net_avg_loss | -35.9840 |
| avg_hold_time_bars | 4.9355 |
| exposure | 0.2261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
