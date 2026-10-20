# EMA Hourly Continuation — WEMIX/USDT P8_26

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2033 |
| net_profit_factor | 0.1754 |
| net_win_rate | 0.2966 |
| gross_profit_factor | 0.4334 |
| gross_win_rate | 0.3182 |
| sharpe_ratio | -21.0149 |
| sortino_ratio | -13.6741 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 3.5272 |
| net_avg_loss | -8.4803 |
| avg_hold_time_bars | 3.5612 |
| exposure | 0.3291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
