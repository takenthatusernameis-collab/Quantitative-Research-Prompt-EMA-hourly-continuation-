# EMA Hourly Continuation — BRETT/USDT P34_55

**Symbol:** BRETT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 830 |
| net_profit_factor | 0.4261 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.7186 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -7.4655 |
| sortino_ratio | -3.1361 |
| max_drawdown | 0.9732 |
| cagr | -0.7815 |
| net_avg_win | 20.7609 |
| net_avg_loss | -35.1742 |
| avg_hold_time_bars | 3.0313 |
| exposure | 0.1211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
