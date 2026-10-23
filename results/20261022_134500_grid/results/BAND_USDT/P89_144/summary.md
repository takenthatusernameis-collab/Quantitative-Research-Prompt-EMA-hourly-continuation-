# EMA Hourly Continuation — BAND/USDT P89_144

**Symbol:** BAND/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.5639 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -4.0374 |
| sortino_ratio | -1.2352 |
| max_drawdown | 0.7800 |
| cagr | -0.4458 |
| net_avg_win | 44.7103 |
| net_avg_loss | -72.1923 |
| avg_hold_time_bars | 5.2511 |
| exposure | 0.1117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
