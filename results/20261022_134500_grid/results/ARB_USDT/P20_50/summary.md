# EMA Hourly Continuation — ARB/USDT P20_50

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.4678 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8656 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -6.8368 |
| sortino_ratio | -2.9986 |
| max_drawdown | 0.9759 |
| cagr | -0.7710 |
| net_avg_win | 19.3051 |
| net_avg_loss | -34.7057 |
| avg_hold_time_bars | 4.7757 |
| exposure | 0.2110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
