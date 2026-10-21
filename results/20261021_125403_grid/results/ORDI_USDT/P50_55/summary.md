# EMA Hourly Continuation — ORDI/USDT P50_55

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.5853 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8046 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -1.7605 |
| sortino_ratio | -0.2725 |
| max_drawdown | 0.2749 |
| cagr | -0.1171 |
| net_avg_win | 71.5451 |
| net_avg_loss | -99.6714 |
| avg_hold_time_bars | 5.0424 |
| exposure | 0.0270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
