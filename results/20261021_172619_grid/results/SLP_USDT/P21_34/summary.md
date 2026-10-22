# EMA Hourly Continuation — SLP/USDT P21_34

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6567 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.9296 |
| sortino_ratio | -0.7951 |
| max_drawdown | 0.6305 |
| cagr | -0.3051 |
| net_avg_win | 68.2055 |
| net_avg_loss | -91.3605 |
| avg_hold_time_bars | 4.9972 |
| exposure | 0.0815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
