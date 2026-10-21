# EMA Hourly Continuation — SOL/USDT P20_50

**Symbol:** SOL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8955 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -3.0377 |
| sortino_ratio | -0.9120 |
| max_drawdown | 0.6628 |
| cagr | -0.3425 |
| net_avg_win | 58.2847 |
| net_avg_loss | -79.0482 |
| avg_hold_time_bars | 7.9095 |
| exposure | 0.1589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
