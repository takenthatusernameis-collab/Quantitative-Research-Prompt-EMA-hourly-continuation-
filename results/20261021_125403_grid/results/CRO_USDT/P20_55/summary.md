# EMA Hourly Continuation — CRO/USDT P20_55

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5834 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.8635 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -3.5872 |
| sortino_ratio | -1.1659 |
| max_drawdown | 0.7481 |
| cagr | -0.4134 |
| net_avg_win | 42.3513 |
| net_avg_loss | -65.1239 |
| avg_hold_time_bars | 9.4186 |
| exposure | 0.2209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
