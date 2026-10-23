# EMA Hourly Continuation — SQD/USDT P34_55

**Symbol:** SQD/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.5787 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9627 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -5.4229 |
| sortino_ratio | -2.1848 |
| max_drawdown | 0.9252 |
| cagr | -0.6515 |
| net_avg_win | 33.8849 |
| net_avg_loss | -52.1425 |
| avg_hold_time_bars | 3.8136 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
