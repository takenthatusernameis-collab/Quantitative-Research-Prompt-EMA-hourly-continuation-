# EMA Hourly Continuation — UNI/USDT P8_89

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7935 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -1.5810 |
| sortino_ratio | -0.5089 |
| max_drawdown | 0.4842 |
| cagr | -0.2097 |
| net_avg_win | 68.3195 |
| net_avg_loss | -84.0873 |
| avg_hold_time_bars | 26.2461 |
| exposure | 0.6060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
