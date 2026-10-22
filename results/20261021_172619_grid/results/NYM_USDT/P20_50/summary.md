# EMA Hourly Continuation — NYM/USDT P20_50

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -4.2883 |
| sortino_ratio | -1.2164 |
| max_drawdown | 0.7653 |
| cagr | -0.4315 |
| net_avg_win | 42.1947 |
| net_avg_loss | -67.7047 |
| avg_hold_time_bars | 13.0581 |
| exposure | 0.2350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
