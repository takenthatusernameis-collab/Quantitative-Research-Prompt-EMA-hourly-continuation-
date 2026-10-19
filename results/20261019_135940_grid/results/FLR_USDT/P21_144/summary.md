# EMA Hourly Continuation — FLR/USDT P21_144

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.4939 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -5.9376 |
| sortino_ratio | -2.1677 |
| max_drawdown | 0.9329 |
| cagr | -0.6578 |
| net_avg_win | 30.7325 |
| net_avg_loss | -47.4747 |
| avg_hold_time_bars | 15.4211 |
| exposure | 0.4795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
