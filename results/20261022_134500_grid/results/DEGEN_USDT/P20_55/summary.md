# EMA Hourly Continuation — DEGEN/USDT P20_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -5.2445 |
| sortino_ratio | -2.2322 |
| max_drawdown | 0.9329 |
| cagr | -0.6549 |
| net_avg_win | 38.4099 |
| net_avg_loss | -51.4690 |
| avg_hold_time_bars | 5.8735 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
