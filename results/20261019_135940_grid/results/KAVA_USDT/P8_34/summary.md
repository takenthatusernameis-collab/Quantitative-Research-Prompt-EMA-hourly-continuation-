# EMA Hourly Continuation — KAVA/USDT P8_34

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1439 |
| net_profit_factor | 0.4182 |
| net_win_rate | 0.4072 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -11.7190 |
| sortino_ratio | -6.2330 |
| max_drawdown | 0.9997 |
| cagr | -0.9605 |
| net_avg_win | 12.2630 |
| net_avg_loss | -20.1444 |
| avg_hold_time_bars | 5.8249 |
| exposure | 0.3810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
