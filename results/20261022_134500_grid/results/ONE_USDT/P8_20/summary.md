# EMA Hourly Continuation — ONE/USDT P8_20

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1743 |
| net_profit_factor | 0.3333 |
| net_win_rate | 0.4223 |
| gross_profit_factor | 0.7355 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -12.0219 |
| sortino_ratio | -7.0899 |
| max_drawdown | 0.9999 |
| cagr | -0.9710 |
| net_avg_win | 6.7905 |
| net_avg_loss | -14.8922 |
| avg_hold_time_bars | 2.6386 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
