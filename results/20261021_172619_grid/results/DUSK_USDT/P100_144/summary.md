# EMA Hourly Continuation — DUSK/USDT P100_144

**Symbol:** DUSK/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8412 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0899 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.8404 |
| sortino_ratio | -0.1987 |
| max_drawdown | 0.2484 |
| cagr | -0.0885 |
| net_avg_win | 78.0108 |
| net_avg_loss | -102.1622 |
| avg_hold_time_bars | 5.9888 |
| exposure | 0.0732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
