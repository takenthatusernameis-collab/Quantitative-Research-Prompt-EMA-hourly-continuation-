# EMA Hourly Continuation — WLD/USDT P21_200

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.8923 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.0940 |
| gross_win_rate | 0.5268 |
| sharpe_ratio | -0.5578 |
| sortino_ratio | -0.1419 |
| max_drawdown | 0.3025 |
| cagr | -0.0678 |
| net_avg_win | 80.2083 |
| net_avg_loss | -100.0736 |
| avg_hold_time_bars | 44.6309 |
| exposure | 0.6431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
