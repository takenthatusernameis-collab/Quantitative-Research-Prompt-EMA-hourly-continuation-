# EMA Hourly Continuation — TWT/USDT P20_21

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.7864 |
| net_win_rate | 0.5676 |
| gross_profit_factor | 1.2961 |
| gross_win_rate | 0.5676 |
| sharpe_ratio | -0.9516 |
| sortino_ratio | -0.1886 |
| max_drawdown | 0.2450 |
| cagr | -0.0820 |
| net_avg_win | 67.8380 |
| net_avg_loss | -113.2187 |
| avg_hold_time_bars | 4.9027 |
| exposure | 0.0412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
