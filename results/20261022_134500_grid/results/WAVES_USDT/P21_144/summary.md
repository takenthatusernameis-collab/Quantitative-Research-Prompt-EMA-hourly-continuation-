# EMA Hourly Continuation — WAVES/USDT P21_144

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.5400 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -5.1666 |
| sortino_ratio | -1.8253 |
| max_drawdown | 0.9039 |
| cagr | -0.5957 |
| net_avg_win | 36.4398 |
| net_avg_loss | -55.4049 |
| avg_hold_time_bars | 17.6661 |
| exposure | 0.5147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
