# EMA Hourly Continuation — SUSHI/USDT P8_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1080 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -6.8659 |
| sortino_ratio | -3.1450 |
| max_drawdown | 0.9798 |
| cagr | -0.7865 |
| net_avg_win | 26.7230 |
| net_avg_loss | -37.8134 |
| avg_hold_time_bars | 9.7991 |
| exposure | 0.4789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
