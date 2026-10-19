# EMA Hourly Continuation — UNI/USDT P26_144

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6156 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9294 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -3.2705 |
| sortino_ratio | -0.9802 |
| max_drawdown | 0.7084 |
| cagr | -0.3853 |
| net_avg_win | 50.6487 |
| net_avg_loss | -75.5063 |
| avg_hold_time_bars | 22.4657 |
| exposure | 0.4759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
