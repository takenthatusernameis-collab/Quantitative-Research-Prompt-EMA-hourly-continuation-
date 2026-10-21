# EMA Hourly Continuation — ZEC/USDT P20_89

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.9564 |
| net_win_rate | 0.5360 |
| gross_profit_factor | 1.1456 |
| gross_win_rate | 0.5360 |
| sharpe_ratio | -0.2383 |
| sortino_ratio | -0.0715 |
| max_drawdown | 0.2487 |
| cagr | -0.0390 |
| net_avg_win | 90.2909 |
| net_avg_loss | -109.0391 |
| avg_hold_time_bars | 17.9327 |
| exposure | 0.3513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
