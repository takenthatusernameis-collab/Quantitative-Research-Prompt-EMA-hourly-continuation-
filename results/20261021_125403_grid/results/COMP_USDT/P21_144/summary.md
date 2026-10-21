# EMA Hourly Continuation — COMP/USDT P21_144

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0386 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -1.4047 |
| sortino_ratio | -0.4174 |
| max_drawdown | 0.4314 |
| cagr | -0.1762 |
| net_avg_win | 69.1129 |
| net_avg_loss | -90.3257 |
| avg_hold_time_bars | 27.0418 |
| exposure | 0.5298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
