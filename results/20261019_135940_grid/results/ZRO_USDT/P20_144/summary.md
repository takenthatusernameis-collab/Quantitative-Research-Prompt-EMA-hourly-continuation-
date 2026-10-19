# EMA Hourly Continuation — ZRO/USDT P20_144

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7050 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -2.5258 |
| sortino_ratio | -0.8048 |
| max_drawdown | 0.5999 |
| cagr | -0.3158 |
| net_avg_win | 61.5740 |
| net_avg_loss | -81.2766 |
| avg_hold_time_bars | 23.6173 |
| exposure | 0.5468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
