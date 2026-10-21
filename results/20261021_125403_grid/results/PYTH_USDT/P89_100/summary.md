# EMA Hourly Continuation — PYTH/USDT P89_100

**Symbol:** PYTH/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 83 |
| net_profit_factor | 0.9506 |
| net_win_rate | 0.5663 |
| gross_profit_factor | 1.2919 |
| gross_win_rate | 0.5663 |
| sharpe_ratio | -0.1147 |
| sortino_ratio | -0.0153 |
| max_drawdown | 0.0879 |
| cagr | -0.0082 |
| net_avg_win | 83.8243 |
| net_avg_loss | -115.1303 |
| avg_hold_time_bars | 4.9880 |
| exposure | 0.0188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
