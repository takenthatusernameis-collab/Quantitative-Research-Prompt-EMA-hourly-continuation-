# EMA Hourly Continuation — W/USDT P20_26

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.7082 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9495 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -1.6905 |
| sortino_ratio | -0.3565 |
| max_drawdown | 0.4050 |
| cagr | -0.1515 |
| net_avg_win | 78.1647 |
| net_avg_loss | -103.4708 |
| avg_hold_time_bars | 4.8203 |
| exposure | 0.0475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
