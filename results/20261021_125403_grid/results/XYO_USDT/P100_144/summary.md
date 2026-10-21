# EMA Hourly Continuation — XYO/USDT P100_144

**Symbol:** XYO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.5265 |
| net_win_rate | 0.4103 |
| gross_profit_factor | 0.7616 |
| gross_win_rate | 0.4103 |
| sharpe_ratio | -3.7501 |
| sortino_ratio | -0.8825 |
| max_drawdown | 0.6491 |
| cagr | -0.3376 |
| net_avg_win | 64.1426 |
| net_avg_loss | -84.7553 |
| avg_hold_time_bars | 6.6154 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
