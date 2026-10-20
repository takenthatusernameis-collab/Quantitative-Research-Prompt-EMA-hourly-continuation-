# EMA Hourly Continuation — TFUEL/USDT P8_12

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1961 |
| net_profit_factor | 0.1910 |
| net_win_rate | 0.3085 |
| gross_profit_factor | 0.5821 |
| gross_win_rate | 0.3779 |
| sharpe_ratio | -21.3140 |
| sortino_ratio | -13.9107 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 3.9027 |
| net_avg_loss | -9.1159 |
| avg_hold_time_bars | 2.1458 |
| exposure | 0.1904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
