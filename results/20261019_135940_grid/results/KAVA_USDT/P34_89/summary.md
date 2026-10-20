# EMA Hourly Continuation — KAVA/USDT P34_89

**Symbol:** KAVA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.5426 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.9776 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -6.9021 |
| sortino_ratio | -2.6804 |
| max_drawdown | 0.9673 |
| cagr | -0.7352 |
| net_avg_win | 34.3508 |
| net_avg_loss | -49.4916 |
| avg_hold_time_bars | 7.5652 |
| exposure | 0.2610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
