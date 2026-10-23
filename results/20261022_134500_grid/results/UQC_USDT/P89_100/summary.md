# EMA Hourly Continuation — UQC/USDT P89_100

**Symbol:** UQC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.0765 |
| net_win_rate | 0.1746 |
| gross_profit_factor | 0.2844 |
| gross_win_rate | 0.2369 |
| sharpe_ratio | -12.0875 |
| sortino_ratio | -3.8588 |
| max_drawdown | 0.9961 |
| cagr | -0.8885 |
| net_avg_win | 11.7870 |
| net_avg_loss | -32.5846 |
| avg_hold_time_bars | 11.6110 |
| exposure | 0.2107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
