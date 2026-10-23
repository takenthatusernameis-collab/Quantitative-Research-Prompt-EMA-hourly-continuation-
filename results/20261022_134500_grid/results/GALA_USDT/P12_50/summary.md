# EMA Hourly Continuation — GALA/USDT P12_50

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.4641 |
| net_win_rate | 0.4325 |
| gross_profit_factor | 0.7945 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -7.8060 |
| sortino_ratio | -3.6773 |
| max_drawdown | 0.9900 |
| cagr | -0.8340 |
| net_avg_win | 17.6988 |
| net_avg_loss | -29.0650 |
| avg_hold_time_bars | 6.4942 |
| exposure | 0.3303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
