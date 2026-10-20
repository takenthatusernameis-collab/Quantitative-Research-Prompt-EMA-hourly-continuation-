# EMA Hourly Continuation — XEC/USDT P50_144

**Symbol:** XEC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.4715 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.7947 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -5.1272 |
| sortino_ratio | -1.6341 |
| max_drawdown | 0.8721 |
| cagr | -0.5478 |
| net_avg_win | 34.9180 |
| net_avg_loss | -55.4799 |
| avg_hold_time_bars | 13.9516 |
| exposure | 0.3258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
