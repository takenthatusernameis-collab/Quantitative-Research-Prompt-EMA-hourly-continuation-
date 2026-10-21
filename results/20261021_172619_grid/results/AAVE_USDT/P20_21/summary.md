# EMA Hourly Continuation — AAVE/USDT P20_21

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 100 |
| net_profit_factor | 0.6649 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -1.3419 |
| sortino_ratio | -0.1919 |
| max_drawdown | 0.2535 |
| cagr | -0.0847 |
| net_avg_win | 84.1600 |
| net_avg_loss | -112.2503 |
| avg_hold_time_bars | 8.7800 |
| exposure | 0.0399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
