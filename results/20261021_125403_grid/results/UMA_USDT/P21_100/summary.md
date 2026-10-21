# EMA Hourly Continuation — UMA/USDT P21_100

**Symbol:** UMA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7425 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -2.1579 |
| sortino_ratio | -0.6964 |
| max_drawdown | 0.5803 |
| cagr | -0.2745 |
| net_avg_win | 63.8251 |
| net_avg_loss | -82.3371 |
| avg_hold_time_bars | 16.7495 |
| exposure | 0.3890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
