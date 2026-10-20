# EMA Hourly Continuation — MERL/USDT P8_200

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.8224 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -0.8938 |
| sortino_ratio | -0.1866 |
| max_drawdown | 0.3116 |
| cagr | -0.0881 |
| net_avg_win | 83.7758 |
| net_avg_loss | -105.5656 |
| avg_hold_time_bars | 84.5625 |
| exposure | 0.8634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
