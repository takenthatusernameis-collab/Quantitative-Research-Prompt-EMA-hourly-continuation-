# EMA Hourly Continuation — ORDI/USDT P55_89

**Symbol:** ORDI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.7074 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -1.8780 |
| sortino_ratio | -0.4421 |
| max_drawdown | 0.4423 |
| cagr | -0.1838 |
| net_avg_win | 74.8915 |
| net_avg_loss | -95.4990 |
| avg_hold_time_bars | 6.7794 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
