# EMA Hourly Continuation — CGPT/USDT P12_55

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.8480 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0513 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -1.2527 |
| sortino_ratio | -0.4340 |
| max_drawdown | 0.4770 |
| cagr | -0.1836 |
| net_avg_win | 74.4551 |
| net_avg_loss | -93.0952 |
| avg_hold_time_bars | 13.3890 |
| exposure | 0.3536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
