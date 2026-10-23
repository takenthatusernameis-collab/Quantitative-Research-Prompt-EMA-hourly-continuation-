# EMA Hourly Continuation — YGG/USDT P20_34

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.4507 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.8196 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -9.7892 |
| sortino_ratio | -4.6909 |
| max_drawdown | 0.9972 |
| cagr | -0.9020 |
| net_avg_win | 16.9396 |
| net_avg_loss | -27.1350 |
| avg_hold_time_bars | 2.8003 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
