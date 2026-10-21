# EMA Hourly Continuation — DCR/USDT P8_100

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.7076 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.8843 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -2.3759 |
| sortino_ratio | -0.7967 |
| max_drawdown | 0.6327 |
| cagr | -0.3077 |
| net_avg_win | 54.9940 |
| net_avg_loss | -70.5606 |
| avg_hold_time_bars | 24.7943 |
| exposure | 0.6272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
