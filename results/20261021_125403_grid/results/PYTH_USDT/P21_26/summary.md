# EMA Hourly Continuation — PYTH/USDT P21_26

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.7142 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.4512 |
| sortino_ratio | -0.2690 |
| max_drawdown | 0.3269 |
| cagr | -0.1161 |
| net_avg_win | 82.2296 |
| net_avg_loss | -107.1896 |
| avg_hold_time_bars | 3.9643 |
| exposure | 0.0303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
