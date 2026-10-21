# EMA Hourly Continuation — WIN/USDT P89_200

**Symbol:** WIN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.5343 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7292 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -2.7996 |
| sortino_ratio | -0.5945 |
| max_drawdown | 0.5027 |
| cagr | -0.2403 |
| net_avg_win | 60.2095 |
| net_avg_loss | -83.6396 |
| avg_hold_time_bars | 19.7085 |
| exposure | 0.1998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
