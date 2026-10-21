# EMA Hourly Continuation — FLR/USDT P26_34

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.4569 |
| net_win_rate | 0.4009 |
| gross_profit_factor | 0.6868 |
| gross_win_rate | 0.4009 |
| sharpe_ratio | -3.8466 |
| sortino_ratio | -0.8392 |
| max_drawdown | 0.6404 |
| cagr | -0.3222 |
| net_avg_win | 56.3795 |
| net_avg_loss | -82.5684 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
