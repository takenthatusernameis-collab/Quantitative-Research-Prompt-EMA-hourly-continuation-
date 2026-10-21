# EMA Hourly Continuation — FLR/USDT P20_89

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.7042 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.6456 |
| sortino_ratio | -0.8841 |
| max_drawdown | 0.6700 |
| cagr | -0.3336 |
| net_avg_win | 57.8520 |
| net_avg_loss | -75.8112 |
| avg_hold_time_bars | 13.4599 |
| exposure | 0.3353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
