# EMA Hourly Continuation — BTC/USDT P20_144

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0262 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -2.2134 |
| sortino_ratio | -0.5836 |
| max_drawdown | 0.5400 |
| cagr | -0.2340 |
| net_avg_win | 58.4170 |
| net_avg_loss | -87.9945 |
| avg_hold_time_bars | 34.4338 |
| exposure | 0.5303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
