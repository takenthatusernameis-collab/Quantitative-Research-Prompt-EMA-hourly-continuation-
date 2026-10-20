# EMA Hourly Continuation — CTC/USDT P8_144

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.6049 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -3.7689 |
| sortino_ratio | -1.2403 |
| max_drawdown | 0.8047 |
| cagr | -0.4500 |
| net_avg_win | 47.0413 |
| net_avg_loss | -67.1455 |
| avg_hold_time_bars | 29.3205 |
| exposure | 0.7277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
