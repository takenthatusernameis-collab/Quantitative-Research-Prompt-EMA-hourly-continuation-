# EMA Hourly Continuation — ZEN/USDT P21_144

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8719 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0523 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -0.8181 |
| sortino_ratio | -0.2271 |
| max_drawdown | 0.3252 |
| cagr | -0.1025 |
| net_avg_win | 84.2656 |
| net_avg_loss | -101.9585 |
| avg_hold_time_bars | 30.5348 |
| exposure | 0.5191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
