# EMA Hourly Continuation — DIA/USDT P26_55

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6465 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8860 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -3.2860 |
| sortino_ratio | -1.0563 |
| max_drawdown | 0.7344 |
| cagr | -0.3831 |
| net_avg_win | 54.5806 |
| net_avg_loss | -72.9822 |
| avg_hold_time_bars | 7.3065 |
| exposure | 0.1683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
