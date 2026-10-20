# EMA Hourly Continuation — ORDI/USDT P8_21

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1701 |
| net_profit_factor | 0.4302 |
| net_win_rate | 0.4198 |
| gross_profit_factor | 0.8269 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -11.6569 |
| sortino_ratio | -6.7819 |
| max_drawdown | 0.9998 |
| cagr | -0.9662 |
| net_avg_win | 10.5732 |
| net_avg_loss | -17.7783 |
| avg_hold_time_bars | 3.0018 |
| exposure | 0.2321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
