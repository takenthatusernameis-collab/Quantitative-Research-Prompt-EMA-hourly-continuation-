# EMA Hourly Continuation — SAFE/USDT P20_21

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.5554 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8020 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -2.3217 |
| sortino_ratio | -0.4380 |
| max_drawdown | 0.3935 |
| cagr | -0.1818 |
| net_avg_win | 63.0136 |
| net_avg_loss | -93.1571 |
| avg_hold_time_bars | 10.9364 |
| exposure | 0.0866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
