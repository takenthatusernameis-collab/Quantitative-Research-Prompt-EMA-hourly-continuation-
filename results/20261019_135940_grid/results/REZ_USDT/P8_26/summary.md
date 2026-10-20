# EMA Hourly Continuation — REZ/USDT P8_26

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1454 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -7.6289 |
| sortino_ratio | -4.1301 |
| max_drawdown | 0.9928 |
| cagr | -0.8632 |
| net_avg_win | 24.5277 |
| net_avg_loss | -33.3281 |
| avg_hold_time_bars | 4.1651 |
| exposure | 0.2794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
