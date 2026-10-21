# EMA Hourly Continuation — ARB/USDT P21_100

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.9076 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1251 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.5668 |
| sortino_ratio | -0.1701 |
| max_drawdown | 0.2817 |
| cagr | -0.0798 |
| net_avg_win | 80.4896 |
| net_avg_loss | -100.9749 |
| avg_hold_time_bars | 20.8750 |
| exposure | 0.4099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
