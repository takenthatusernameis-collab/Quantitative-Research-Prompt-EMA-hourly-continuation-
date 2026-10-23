# EMA Hourly Continuation — CARV/USDT P34_89

**Symbol:** CARV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.4981 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -5.0559 |
| sortino_ratio | -1.7492 |
| max_drawdown | 0.8256 |
| cagr | -0.5644 |
| net_avg_win | 37.6116 |
| net_avg_loss | -60.1244 |
| avg_hold_time_bars | 8.5113 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
