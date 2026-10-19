# EMA Hourly Continuation — SUN/USDT P8_200

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.4978 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8910 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -3.8785 |
| sortino_ratio | -0.9516 |
| max_drawdown | 0.7214 |
| cagr | -0.3896 |
| net_avg_win | 49.0180 |
| net_avg_loss | -80.5666 |
| avg_hold_time_bars | 55.5594 |
| exposure | 0.8046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
