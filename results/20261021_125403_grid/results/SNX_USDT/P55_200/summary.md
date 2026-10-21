# EMA Hourly Continuation — SNX/USDT P55_200

**Symbol:** SNX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.9003 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.0926 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -0.5389 |
| sortino_ratio | -0.1326 |
| max_drawdown | 0.2171 |
| cagr | -0.0621 |
| net_avg_win | 88.0644 |
| net_avg_loss | -106.9030 |
| avg_hold_time_bars | 26.3720 |
| exposure | 0.3497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
