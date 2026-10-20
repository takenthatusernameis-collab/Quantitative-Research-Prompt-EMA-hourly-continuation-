# EMA Hourly Continuation — MOG/USDT P12_50

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.7143 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9681 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -4.6822 |
| sortino_ratio | -2.1509 |
| max_drawdown | 0.9064 |
| cagr | -0.6395 |
| net_avg_win | 49.3350 |
| net_avg_loss | -61.9075 |
| avg_hold_time_bars | 7.4964 |
| exposure | 0.3611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
