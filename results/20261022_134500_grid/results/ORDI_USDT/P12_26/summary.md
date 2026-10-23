# EMA Hourly Continuation — ORDI/USDT P12_26

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1442 |
| net_profit_factor | 0.4624 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -9.9976 |
| sortino_ratio | -5.3353 |
| max_drawdown | 0.9988 |
| cagr | -0.9304 |
| net_avg_win | 13.7242 |
| net_avg_loss | -22.7683 |
| avg_hold_time_bars | 2.9584 |
| exposure | 0.1939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
