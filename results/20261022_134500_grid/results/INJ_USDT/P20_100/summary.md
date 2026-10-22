# EMA Hourly Continuation — INJ/USDT P20_100

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.6569 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -3.5871 |
| sortino_ratio | -1.3404 |
| max_drawdown | 0.7987 |
| cagr | -0.4693 |
| net_avg_win | 45.2383 |
| net_avg_loss | -63.5837 |
| avg_hold_time_bars | 12.2678 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
