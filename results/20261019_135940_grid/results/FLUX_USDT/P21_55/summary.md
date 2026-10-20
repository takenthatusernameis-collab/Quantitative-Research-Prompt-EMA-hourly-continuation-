# EMA Hourly Continuation — FLUX/USDT P21_55

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 966 |
| net_profit_factor | 0.5270 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -6.6001 |
| sortino_ratio | -2.8726 |
| max_drawdown | 0.9719 |
| cagr | -0.7583 |
| net_avg_win | 24.2746 |
| net_avg_loss | -39.5077 |
| avg_hold_time_bars | 4.7091 |
| exposure | 0.2068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
