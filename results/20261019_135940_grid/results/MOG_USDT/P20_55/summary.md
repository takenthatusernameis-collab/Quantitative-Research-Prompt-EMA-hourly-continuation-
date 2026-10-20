# EMA Hourly Continuation — MOG/USDT P20_55

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.6605 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -5.1555 |
| sortino_ratio | -2.2260 |
| max_drawdown | 0.9190 |
| cagr | -0.6600 |
| net_avg_win | 44.0089 |
| net_avg_loss | -58.1544 |
| avg_hold_time_bars | 5.7595 |
| exposure | 0.2488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
