# EMA Hourly Continuation — CHZ/USDT P21_144

**Symbol:** CHZ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9197 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.1224 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -0.4575 |
| sortino_ratio | -0.1227 |
| max_drawdown | 0.3368 |
| cagr | -0.0590 |
| net_avg_win | 88.6149 |
| net_avg_loss | -108.1756 |
| avg_hold_time_bars | 34.5694 |
| exposure | 0.5437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
