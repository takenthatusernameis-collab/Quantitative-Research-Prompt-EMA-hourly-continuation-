# EMA Hourly Continuation — GRAM/USDT P8_34

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6606 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -3.4815 |
| sortino_ratio | -1.2701 |
| max_drawdown | 0.7833 |
| cagr | -0.4414 |
| net_avg_win | 48.2385 |
| net_avg_loss | -66.5783 |
| avg_hold_time_bars | 8.6062 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
