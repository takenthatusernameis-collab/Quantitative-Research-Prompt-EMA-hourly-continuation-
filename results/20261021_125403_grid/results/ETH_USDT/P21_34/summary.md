# EMA Hourly Continuation — ETH/USDT P21_34

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5427 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9114 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -2.8518 |
| sortino_ratio | -0.6176 |
| max_drawdown | 0.5166 |
| cagr | -0.2463 |
| net_avg_win | 55.8670 |
| net_avg_loss | -93.4254 |
| avg_hold_time_bars | 5.4317 |
| exposure | 0.0560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
