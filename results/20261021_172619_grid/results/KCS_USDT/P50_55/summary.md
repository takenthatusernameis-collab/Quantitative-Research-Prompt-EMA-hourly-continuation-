# EMA Hourly Continuation — KCS/USDT P50_55

**Symbol:** KCS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.3191 |
| net_win_rate | 0.3857 |
| gross_profit_factor | 0.6528 |
| gross_win_rate | 0.3857 |
| sharpe_ratio | -4.0149 |
| sortino_ratio | -0.6980 |
| max_drawdown | 0.5624 |
| cagr | -0.2781 |
| net_avg_win | 48.5026 |
| net_avg_loss | -95.4346 |
| avg_hold_time_bars | 5.8786 |
| exposure | 0.0374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
