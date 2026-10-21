# EMA Hourly Continuation — DCR/USDT P21_144

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0109 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.3483 |
| sortino_ratio | -0.4183 |
| max_drawdown | 0.4495 |
| cagr | -0.1769 |
| net_avg_win | 61.1272 |
| net_avg_loss | -80.9208 |
| avg_hold_time_bars | 22.4565 |
| exposure | 0.4786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
