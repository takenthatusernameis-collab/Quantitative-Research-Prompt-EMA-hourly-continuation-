# EMA Hourly Continuation — GRT/USDT P34_89

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.5531 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -4.8086 |
| sortino_ratio | -1.8111 |
| max_drawdown | 0.8950 |
| cagr | -0.5798 |
| net_avg_win | 32.5966 |
| net_avg_loss | -52.9670 |
| avg_hold_time_bars | 7.0365 |
| exposure | 0.2267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
