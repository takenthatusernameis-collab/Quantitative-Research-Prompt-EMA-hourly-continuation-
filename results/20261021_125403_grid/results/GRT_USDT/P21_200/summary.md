# EMA Hourly Continuation — GRT/USDT P21_200

**Symbol:** GRT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.9159 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0693 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.4134 |
| sortino_ratio | -0.0964 |
| max_drawdown | 0.2368 |
| cagr | -0.0467 |
| net_avg_win | 89.6293 |
| net_avg_loss | -106.3352 |
| avg_hold_time_bars | 52.6755 |
| exposure | 0.6317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
