# EMA Hourly Continuation — POPCAT/USDT P8_20

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.5274 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.7983 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -10.1124 |
| sortino_ratio | -5.9023 |
| max_drawdown | 0.9981 |
| cagr | -0.9442 |
| net_avg_win | 17.3769 |
| net_avg_loss | -25.2017 |
| avg_hold_time_bars | 2.8364 |
| exposure | 0.2216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
