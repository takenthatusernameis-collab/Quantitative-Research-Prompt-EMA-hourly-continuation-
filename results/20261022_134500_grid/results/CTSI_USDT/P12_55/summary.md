# EMA Hourly Continuation — CTSI/USDT P12_55

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1032 |
| net_profit_factor | 0.6040 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -5.9499 |
| sortino_ratio | -2.6977 |
| max_drawdown | 0.9616 |
| cagr | -0.7227 |
| net_avg_win | 30.5125 |
| net_avg_loss | -43.9254 |
| avg_hold_time_bars | 7.9176 |
| exposure | 0.3714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
