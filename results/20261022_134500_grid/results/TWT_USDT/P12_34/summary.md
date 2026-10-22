# EMA Hourly Continuation — TWT/USDT P12_34

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1367 |
| net_profit_factor | 0.3788 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.8554 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -10.2828 |
| sortino_ratio | -5.3486 |
| max_drawdown | 0.9990 |
| cagr | -0.9343 |
| net_avg_win | 9.9530 |
| net_avg_loss | -21.2987 |
| avg_hold_time_bars | 4.2129 |
| exposure | 0.2618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
