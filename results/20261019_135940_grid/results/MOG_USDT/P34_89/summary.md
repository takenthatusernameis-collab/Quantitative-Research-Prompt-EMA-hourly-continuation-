# EMA Hourly Continuation — MOG/USDT P34_89

**Symbol:** MOG/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.6698 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9342 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -3.4895 |
| sortino_ratio | -1.2964 |
| max_drawdown | 0.7611 |
| cagr | -0.4601 |
| net_avg_win | 49.5377 |
| net_avg_loss | -70.1156 |
| avg_hold_time_bars | 6.7661 |
| exposure | 0.2143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
