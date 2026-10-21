# EMA Hourly Continuation — EUL/USDT P8_200

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8485 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8701 |
| sortino_ratio | -0.2315 |
| max_drawdown | 0.2726 |
| cagr | -0.1032 |
| net_avg_win | 77.4988 |
| net_avg_loss | -91.3344 |
| avg_hold_time_bars | 46.7139 |
| exposure | 0.7347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
