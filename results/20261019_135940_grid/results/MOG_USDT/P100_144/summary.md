# EMA Hourly Continuation — MOG/USDT P100_144

**Symbol:** MOG/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.5929 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8857 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -4.3839 |
| sortino_ratio | -1.4011 |
| max_drawdown | 0.7959 |
| cagr | -0.4869 |
| net_avg_win | 54.6202 |
| net_avg_loss | -74.9217 |
| avg_hold_time_bars | 3.9335 |
| exposure | 0.0911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
