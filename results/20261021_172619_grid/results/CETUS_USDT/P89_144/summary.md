# EMA Hourly Continuation — CETUS/USDT P89_144

**Symbol:** CETUS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7963 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0234 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -1.2899 |
| sortino_ratio | -0.3070 |
| max_drawdown | 0.3927 |
| cagr | -0.1322 |
| net_avg_win | 84.5656 |
| net_avg_loss | -106.9712 |
| avg_hold_time_bars | 7.6931 |
| exposure | 0.0964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
