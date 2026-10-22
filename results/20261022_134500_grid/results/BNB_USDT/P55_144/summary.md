# EMA Hourly Continuation — BNB/USDT P55_144

**Symbol:** BNB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.3623 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -6.9064 |
| sortino_ratio | -2.3128 |
| max_drawdown | 0.9493 |
| cagr | -0.6901 |
| net_avg_win | 22.0515 |
| net_avg_loss | -47.0035 |
| avg_hold_time_bars | 9.0696 |
| exposure | 0.2309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
