# EMA Hourly Continuation — ORDI/USDT P8_12

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.8964 |
| net_win_rate | 0.5469 |
| gross_profit_factor | 1.2072 |
| gross_win_rate | 0.5469 |
| sharpe_ratio | -0.5452 |
| sortino_ratio | -0.1265 |
| max_drawdown | 0.2210 |
| cagr | -0.0585 |
| net_avg_win | 86.8941 |
| net_avg_loss | -116.9922 |
| avg_hold_time_bars | 4.7266 |
| exposure | 0.0550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
