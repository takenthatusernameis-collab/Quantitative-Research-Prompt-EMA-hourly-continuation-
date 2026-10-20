# EMA Hourly Continuation — G/USDT P20_89

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5200 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -4.7648 |
| sortino_ratio | -1.6617 |
| max_drawdown | 0.8356 |
| cagr | -0.5501 |
| net_avg_win | 37.6412 |
| net_avg_loss | -57.9563 |
| avg_hold_time_bars | 16.8068 |
| exposure | 0.4710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
