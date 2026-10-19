# EMA Hourly Continuation — BCH/USDT P55_89

**Symbol:** BCH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.3595 |
| net_win_rate | 0.4219 |
| gross_profit_factor | 0.7565 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -8.1664 |
| sortino_ratio | -3.0980 |
| max_drawdown | 0.9796 |
| cagr | -0.7879 |
| net_avg_win | 18.5109 |
| net_avg_loss | -37.5778 |
| avg_hold_time_bars | 3.6577 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
