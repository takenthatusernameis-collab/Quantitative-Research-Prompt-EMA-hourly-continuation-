# EMA Hourly Continuation — THETA/USDT P21_26

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.2163 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.6366 |
| gross_win_rate | 0.3873 |
| sharpe_ratio | -14.9840 |
| sortino_ratio | -7.4146 |
| max_drawdown | 1.0000 |
| cagr | -0.9822 |
| net_avg_win | 7.2067 |
| net_avg_loss | -16.6577 |
| avg_hold_time_bars | 1.8259 |
| exposure | 0.0954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
