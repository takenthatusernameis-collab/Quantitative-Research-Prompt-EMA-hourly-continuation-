# EMA Hourly Continuation — SUI/USDT P100_144

**Symbol:** SUI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.5823 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -2.2668 |
| sortino_ratio | -0.4531 |
| max_drawdown | 0.4119 |
| cagr | -0.1875 |
| net_avg_win | 64.3717 |
| net_avg_loss | -89.2529 |
| avg_hold_time_bars | 6.2792 |
| exposure | 0.0562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
