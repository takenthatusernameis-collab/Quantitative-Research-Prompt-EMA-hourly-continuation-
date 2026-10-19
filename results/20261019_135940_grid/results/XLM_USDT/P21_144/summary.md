# EMA Hourly Continuation — XLM/USDT P21_144

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.4261 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8076 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -4.7112 |
| sortino_ratio | -1.4349 |
| max_drawdown | 0.8487 |
| cagr | -0.5200 |
| net_avg_win | 28.5355 |
| net_avg_loss | -54.5213 |
| avg_hold_time_bars | 24.8422 |
| exposure | 0.5510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
