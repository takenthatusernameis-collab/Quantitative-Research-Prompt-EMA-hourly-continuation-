# EMA Hourly Continuation — ZRX/USDT P12_100

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.6303 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -3.8563 |
| sortino_ratio | -1.3535 |
| max_drawdown | 0.8146 |
| cagr | -0.4809 |
| net_avg_win | 46.0351 |
| net_avg_loss | -65.9738 |
| avg_hold_time_bars | 20.0841 |
| exposure | 0.5751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
