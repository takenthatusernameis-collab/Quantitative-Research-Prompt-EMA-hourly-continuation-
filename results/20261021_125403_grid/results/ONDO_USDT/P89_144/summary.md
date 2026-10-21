# EMA Hourly Continuation — ONDO/USDT P89_144

**Symbol:** ONDO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8196 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0508 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -0.9746 |
| sortino_ratio | -0.2288 |
| max_drawdown | 0.2911 |
| cagr | -0.1005 |
| net_avg_win | 77.4304 |
| net_avg_loss | -100.3291 |
| avg_hold_time_bars | 7.2782 |
| exposure | 0.0880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
