# EMA Hourly Continuation — ORDI/USDT P20_89

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.6344 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -4.4742 |
| sortino_ratio | -1.7103 |
| max_drawdown | 0.8757 |
| cagr | -0.5543 |
| net_avg_win | 44.4573 |
| net_avg_loss | -60.1447 |
| avg_hold_time_bars | 11.1785 |
| exposure | 0.3730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
