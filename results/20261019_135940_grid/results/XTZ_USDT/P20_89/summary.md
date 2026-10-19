# EMA Hourly Continuation — XTZ/USDT P20_89

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.5751 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9806 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -4.5726 |
| sortino_ratio | -1.6946 |
| max_drawdown | 0.8837 |
| cagr | -0.5661 |
| net_avg_win | 35.0152 |
| net_avg_loss | -56.2446 |
| avg_hold_time_bars | 13.5581 |
| exposure | 0.4351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
