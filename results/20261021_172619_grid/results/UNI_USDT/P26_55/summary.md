# EMA Hourly Continuation — UNI/USDT P26_55

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6782 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -2.3684 |
| sortino_ratio | -0.6589 |
| max_drawdown | 0.5433 |
| cagr | -0.2606 |
| net_avg_win | 62.5679 |
| net_avg_loss | -82.1592 |
| avg_hold_time_bars | 7.8342 |
| exposure | 0.1353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
