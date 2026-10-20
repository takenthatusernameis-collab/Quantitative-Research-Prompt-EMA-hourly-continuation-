# EMA Hourly Continuation — NYM/USDT P26_100

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.2785 |
| net_win_rate | 0.3494 |
| gross_profit_factor | 0.5925 |
| gross_win_rate | 0.3787 |
| sharpe_ratio | -8.8157 |
| sortino_ratio | -2.9949 |
| max_drawdown | 0.9822 |
| cagr | -0.7950 |
| net_avg_win | 18.6641 |
| net_avg_loss | -35.9839 |
| avg_hold_time_bars | 13.6437 |
| exposure | 0.3603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
