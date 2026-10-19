# EMA Hourly Continuation — XLM/USDT P8_50

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1153 |
| net_profit_factor | 0.3911 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -7.5273 |
| sortino_ratio | -3.5686 |
| max_drawdown | 0.9887 |
| cagr | -0.8310 |
| net_avg_win | 11.9331 |
| net_avg_loss | -26.1406 |
| avg_hold_time_bars | 8.7129 |
| exposure | 0.4566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
