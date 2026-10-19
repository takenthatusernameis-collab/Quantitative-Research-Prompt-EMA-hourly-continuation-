# EMA Hourly Continuation — GRAM/USDT P20_200

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5156 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8700 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -4.0936 |
| sortino_ratio | -1.1827 |
| max_drawdown | 0.7725 |
| cagr | -0.4290 |
| net_avg_win | 43.2112 |
| net_avg_loss | -67.7767 |
| avg_hold_time_bars | 32.8389 |
| exposure | 0.6210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
