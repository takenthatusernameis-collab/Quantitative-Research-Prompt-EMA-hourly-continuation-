# EMA Hourly Continuation — YGG/USDT P21_144

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6763 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.8243 |
| sortino_ratio | -0.9013 |
| max_drawdown | 0.6635 |
| cagr | -0.3456 |
| net_avg_win | 56.4854 |
| net_avg_loss | -75.4462 |
| avg_hold_time_bars | 22.7832 |
| exposure | 0.5279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
