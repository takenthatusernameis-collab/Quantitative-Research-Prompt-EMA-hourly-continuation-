# EMA Hourly Continuation — XCN/USDT P21_144

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6876 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -2.5599 |
| sortino_ratio | -0.7709 |
| max_drawdown | 0.5901 |
| cagr | -0.2988 |
| net_avg_win | 63.0342 |
| net_avg_loss | -77.0813 |
| avg_hold_time_bars | 22.9446 |
| exposure | 0.4704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
