# EMA Hourly Continuation — XLM/USDT P20_50

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6592 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9841 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.6978 |
| sortino_ratio | -0.8551 |
| max_drawdown | 0.6280 |
| cagr | -0.3230 |
| net_avg_win | 49.9244 |
| net_avg_loss | -74.8072 |
| avg_hold_time_bars | 7.9446 |
| exposure | 0.1759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
