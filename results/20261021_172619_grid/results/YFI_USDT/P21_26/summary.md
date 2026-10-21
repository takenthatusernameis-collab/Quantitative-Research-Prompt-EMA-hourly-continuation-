# EMA Hourly Continuation — YFI/USDT P21_26

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.4245 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.7842 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -4.5277 |
| sortino_ratio | -1.1382 |
| max_drawdown | 0.7406 |
| cagr | -0.4106 |
| net_avg_win | 41.4680 |
| net_avg_loss | -74.8351 |
| avg_hold_time_bars | 4.5132 |
| exposure | 0.0617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
