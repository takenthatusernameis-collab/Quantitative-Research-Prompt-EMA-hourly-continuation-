# EMA Hourly Continuation — POPCAT/USDT P8_50

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.8104 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9663 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.9115 |
| sortino_ratio | -0.7206 |
| max_drawdown | 0.5430 |
| cagr | -0.2847 |
| net_avg_win | 74.8891 |
| net_avg_loss | -88.7872 |
| avg_hold_time_bars | 14.3250 |
| exposure | 0.4540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
