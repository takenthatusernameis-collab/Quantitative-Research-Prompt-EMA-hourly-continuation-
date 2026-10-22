# EMA Hourly Continuation — BNB/USDT P21_89

**Symbol:** BNB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.3473 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -8.1919 |
| sortino_ratio | -3.1529 |
| max_drawdown | 0.9845 |
| cagr | -0.8083 |
| net_avg_win | 15.8673 |
| net_avg_loss | -35.8156 |
| avg_hold_time_bars | 10.0826 |
| exposure | 0.3442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
