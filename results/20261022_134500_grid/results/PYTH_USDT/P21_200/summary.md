# EMA Hourly Continuation — PYTH/USDT P21_200

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.8678 |
| net_win_rate | 0.5240 |
| gross_profit_factor | 1.0963 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -0.7647 |
| sortino_ratio | -0.1941 |
| max_drawdown | 0.3070 |
| cagr | -0.0882 |
| net_avg_win | 82.8547 |
| net_avg_loss | -105.0870 |
| avg_hold_time_bars | 47.6230 |
| exposure | 0.6775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
