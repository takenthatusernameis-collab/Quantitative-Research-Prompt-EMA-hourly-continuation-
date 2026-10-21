# EMA Hourly Continuation — LTC/USDT P21_200

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.6312 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8222 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -2.2275 |
| sortino_ratio | -0.5251 |
| max_drawdown | 0.4750 |
| cagr | -0.2140 |
| net_avg_win | 61.6290 |
| net_avg_loss | -82.5701 |
| avg_hold_time_bars | 48.8036 |
| exposure | 0.6100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
