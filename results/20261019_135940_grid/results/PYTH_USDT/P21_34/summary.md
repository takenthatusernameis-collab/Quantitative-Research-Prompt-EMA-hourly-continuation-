# EMA Hourly Continuation — PYTH/USDT P21_34

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.4343 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -8.9659 |
| sortino_ratio | -4.2072 |
| max_drawdown | 0.9951 |
| cagr | -0.8793 |
| net_avg_win | 15.5608 |
| net_avg_loss | -28.4643 |
| avg_hold_time_bars | 2.3580 |
| exposure | 0.1189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
