# EMA Hourly Continuation — KAS/USDT P8_100

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9329 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -4.4628 |
| sortino_ratio | -1.6886 |
| max_drawdown | 0.8772 |
| cagr | -0.5616 |
| net_avg_win | 37.9687 |
| net_avg_loss | -57.1677 |
| avg_hold_time_bars | 19.9221 |
| exposure | 0.6629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
