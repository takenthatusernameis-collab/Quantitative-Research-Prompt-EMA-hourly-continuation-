# EMA Hourly Continuation — IOST/USDT P89_200

**Symbol:** IOST/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6230 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0982 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -2.7758 |
| sortino_ratio | -0.7755 |
| max_drawdown | 0.6196 |
| cagr | -0.3112 |
| net_avg_win | 50.9786 |
| net_avg_loss | -83.5286 |
| avg_hold_time_bars | 11.1846 |
| exposure | 0.1983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
