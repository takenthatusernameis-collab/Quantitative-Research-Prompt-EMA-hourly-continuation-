# EMA Hourly Continuation — AR/USDT P34_100

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7300 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -1.9955 |
| sortino_ratio | -0.5912 |
| max_drawdown | 0.5033 |
| cagr | -0.2386 |
| net_avg_win | 65.0530 |
| net_avg_loss | -81.2326 |
| avg_hold_time_bars | 13.8866 |
| exposure | 0.2727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
