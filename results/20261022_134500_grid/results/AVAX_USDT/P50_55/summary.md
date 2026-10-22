# EMA Hourly Continuation — AVAX/USDT P50_55

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.1735 |
| net_win_rate | 0.3355 |
| gross_profit_factor | 0.6152 |
| gross_win_rate | 0.3931 |
| sharpe_ratio | -13.2677 |
| sortino_ratio | -5.6008 |
| max_drawdown | 0.9996 |
| cagr | -0.9548 |
| net_avg_win | 8.0109 |
| net_avg_loss | -23.3038 |
| avg_hold_time_bars | 1.7209 |
| exposure | 0.0611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
