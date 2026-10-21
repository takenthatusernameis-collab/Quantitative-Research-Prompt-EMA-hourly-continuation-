# EMA Hourly Continuation — MERL/USDT P20_21

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.8151 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0940 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -0.8808 |
| sortino_ratio | -0.1715 |
| max_drawdown | 0.2617 |
| cagr | -0.0758 |
| net_avg_win | 83.0881 |
| net_avg_loss | -111.3154 |
| avg_hold_time_bars | 4.3077 |
| exposure | 0.0357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
