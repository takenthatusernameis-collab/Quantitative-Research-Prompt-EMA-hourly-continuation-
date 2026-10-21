# EMA Hourly Continuation — PYTH/USDT P20_34

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6828 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9075 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.3438 |
| sortino_ratio | -0.6123 |
| max_drawdown | 0.5153 |
| cagr | -0.2443 |
| net_avg_win | 69.2512 |
| net_avg_loss | -89.4575 |
| avg_hold_time_bars | 4.7433 |
| exposure | 0.0722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
