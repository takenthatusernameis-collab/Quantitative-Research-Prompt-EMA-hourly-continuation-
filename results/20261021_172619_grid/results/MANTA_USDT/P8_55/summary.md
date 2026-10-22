# EMA Hourly Continuation — MANTA/USDT P8_55

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.7949 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.0276 |
| sortino_ratio | -0.7365 |
| max_drawdown | 0.5819 |
| cagr | -0.2887 |
| net_avg_win | 69.8312 |
| net_avg_loss | -85.9672 |
| avg_hold_time_bars | 18.2062 |
| exposure | 0.5338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
