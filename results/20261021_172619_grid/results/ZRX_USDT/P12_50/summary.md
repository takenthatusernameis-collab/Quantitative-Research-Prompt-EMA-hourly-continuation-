# EMA Hourly Continuation — ZRX/USDT P12_50

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.6792 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -3.4701 |
| sortino_ratio | -1.3617 |
| max_drawdown | 0.8029 |
| cagr | -0.4654 |
| net_avg_win | 46.3410 |
| net_avg_loss | -63.0111 |
| avg_hold_time_bars | 9.9350 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
