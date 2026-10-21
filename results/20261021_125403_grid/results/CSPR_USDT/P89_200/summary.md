# EMA Hourly Continuation — CSPR/USDT P89_200

**Symbol:** CSPR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7964 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0021 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.3057 |
| sortino_ratio | -0.3420 |
| max_drawdown | 0.3507 |
| cagr | -0.1467 |
| net_avg_win | 76.5522 |
| net_avg_loss | -96.6936 |
| avg_hold_time_bars | 13.1672 |
| exposure | 0.2005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
