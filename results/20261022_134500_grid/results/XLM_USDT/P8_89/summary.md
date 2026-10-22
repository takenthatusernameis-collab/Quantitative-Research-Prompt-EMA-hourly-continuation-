# EMA Hourly Continuation — XLM/USDT P8_89

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5114 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -4.7919 |
| sortino_ratio | -1.8058 |
| max_drawdown | 0.8992 |
| cagr | -0.5887 |
| net_avg_win | 26.7687 |
| net_avg_loss | -48.3288 |
| avg_hold_time_bars | 19.3714 |
| exposure | 0.6401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
