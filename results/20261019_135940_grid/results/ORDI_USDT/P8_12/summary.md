# EMA Hourly Continuation — ORDI/USDT P8_12

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1936 |
| net_profit_factor | 0.2625 |
| net_win_rate | 0.3714 |
| gross_profit_factor | 0.6881 |
| gross_win_rate | 0.4029 |
| sharpe_ratio | -17.7130 |
| sortino_ratio | -11.2099 |
| max_drawdown | 1.0000 |
| cagr | -0.9974 |
| net_avg_win | 4.9495 |
| net_avg_loss | -11.1411 |
| avg_hold_time_bars | 1.7815 |
| exposure | 0.1568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
