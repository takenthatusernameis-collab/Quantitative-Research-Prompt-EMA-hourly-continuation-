# EMA Hourly Continuation — XEC/USDT P8_34

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1428 |
| net_profit_factor | 0.5037 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -9.5971 |
| sortino_ratio | -5.1270 |
| max_drawdown | 0.9982 |
| cagr | -0.9175 |
| net_avg_win | 16.0279 |
| net_avg_loss | -25.2653 |
| avg_hold_time_bars | 5.6870 |
| exposure | 0.3675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
