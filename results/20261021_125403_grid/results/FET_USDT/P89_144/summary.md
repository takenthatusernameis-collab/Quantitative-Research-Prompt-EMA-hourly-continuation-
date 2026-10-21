# EMA Hourly Continuation — FET/USDT P89_144

**Symbol:** FET/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.7550 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.2948 |
| sortino_ratio | -0.2740 |
| max_drawdown | 0.2906 |
| cagr | -0.1185 |
| net_avg_win | 78.1548 |
| net_avg_loss | -98.8973 |
| avg_hold_time_bars | 10.0046 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
