# EMA Hourly Continuation — YFI/USDT P20_100

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -3.0744 |
| sortino_ratio | -1.0228 |
| max_drawdown | 0.7083 |
| cagr | -0.3762 |
| net_avg_win | 55.0334 |
| net_avg_loss | -75.0816 |
| avg_hold_time_bars | 17.2330 |
| exposure | 0.4250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
