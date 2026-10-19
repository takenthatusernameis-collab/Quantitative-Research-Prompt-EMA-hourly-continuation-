# EMA Hourly Continuation — KCS/USDT P20_100

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.2899 |
| net_win_rate | 0.3847 |
| gross_profit_factor | 0.8000 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -8.9820 |
| sortino_ratio | -3.2260 |
| max_drawdown | 0.9866 |
| cagr | -0.8173 |
| net_avg_win | 16.2982 |
| net_avg_loss | -35.1537 |
| avg_hold_time_bars | 15.0530 |
| exposure | 0.4393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
