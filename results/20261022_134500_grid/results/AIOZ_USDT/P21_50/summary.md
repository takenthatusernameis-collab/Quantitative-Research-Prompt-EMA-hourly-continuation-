# EMA Hourly Continuation — AIOZ/USDT P21_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.6182 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -7.0334 |
| sortino_ratio | -3.2388 |
| max_drawdown | 0.9821 |
| cagr | -0.7944 |
| net_avg_win | 32.2902 |
| net_avg_loss | -44.3077 |
| avg_hold_time_bars | 4.5448 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
