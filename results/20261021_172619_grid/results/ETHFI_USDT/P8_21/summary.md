# EMA Hourly Continuation — ETHFI/USDT P8_21

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8061 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0185 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.5075 |
| sortino_ratio | -0.4868 |
| max_drawdown | 0.4664 |
| cagr | -0.2019 |
| net_avg_win | 70.2055 |
| net_avg_loss | -89.1862 |
| avg_hold_time_bars | 5.5494 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
