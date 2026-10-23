# EMA Hourly Continuation — LQTY/USDT P100_144

**Symbol:** LQTY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5271 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.9110 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -4.7072 |
| sortino_ratio | -1.5173 |
| max_drawdown | 0.8378 |
| cagr | -0.5133 |
| net_avg_win | 39.3881 |
| net_avg_loss | -62.7996 |
| avg_hold_time_bars | 4.1985 |
| exposure | 0.0986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
