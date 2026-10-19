# EMA Hourly Continuation — BDX/USDT P12_100

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1248 |
| net_profit_factor | 0.3369 |
| net_win_rate | 0.3149 |
| gross_profit_factor | 0.7136 |
| gross_win_rate | 0.3638 |
| sharpe_ratio | -15.9968 |
| sortino_ratio | -8.2327 |
| max_drawdown | 1.0000 |
| cagr | -0.9887 |
| net_avg_win | 12.9291 |
| net_avg_loss | -17.6386 |
| avg_hold_time_bars | 7.2708 |
| exposure | 0.4125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
