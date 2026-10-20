# EMA Hourly Continuation — DBR/USDT P21_26

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.2897 |
| net_win_rate | 0.3627 |
| gross_profit_factor | 0.9581 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -12.5365 |
| sortino_ratio | -5.6507 |
| max_drawdown | 0.9975 |
| cagr | -0.9497 |
| net_avg_win | 14.7430 |
| net_avg_loss | -28.9574 |
| avg_hold_time_bars | 3.2917 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
