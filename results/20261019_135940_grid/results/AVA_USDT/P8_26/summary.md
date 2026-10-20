# EMA Hourly Continuation — AVA/USDT P8_26

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1476 |
| net_profit_factor | 0.3874 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8256 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -10.6318 |
| sortino_ratio | -5.7556 |
| max_drawdown | 0.9993 |
| cagr | -0.9443 |
| net_avg_win | 9.9210 |
| net_avg_loss | -19.4429 |
| avg_hold_time_bars | 3.7988 |
| exposure | 0.2549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
