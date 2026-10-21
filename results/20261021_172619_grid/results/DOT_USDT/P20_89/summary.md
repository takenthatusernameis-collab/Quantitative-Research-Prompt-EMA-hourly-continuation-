# EMA Hourly Continuation — DOT/USDT P20_89

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8272 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0524 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.2441 |
| sortino_ratio | -0.3815 |
| max_drawdown | 0.4170 |
| cagr | -0.1624 |
| net_avg_win | 73.4623 |
| net_avg_loss | -94.0345 |
| avg_hold_time_bars | 18.5319 |
| exposure | 0.3833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
