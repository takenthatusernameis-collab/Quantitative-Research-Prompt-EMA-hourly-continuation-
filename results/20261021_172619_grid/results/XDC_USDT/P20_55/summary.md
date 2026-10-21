# EMA Hourly Continuation — XDC/USDT P20_55

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8934 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -3.4584 |
| sortino_ratio | -1.0415 |
| max_drawdown | 0.7006 |
| cagr | -0.3793 |
| net_avg_win | 42.9012 |
| net_avg_loss | -68.9259 |
| avg_hold_time_bars | 8.9502 |
| exposure | 0.1798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
