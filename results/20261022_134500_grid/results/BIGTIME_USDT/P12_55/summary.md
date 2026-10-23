# EMA Hourly Continuation — BIGTIME/USDT P12_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.6650 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -4.1588 |
| sortino_ratio | -1.8071 |
| max_drawdown | 0.8872 |
| cagr | -0.5778 |
| net_avg_win | 37.4460 |
| net_avg_loss | -54.4518 |
| avg_hold_time_bars | 8.5575 |
| exposure | 0.3702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
