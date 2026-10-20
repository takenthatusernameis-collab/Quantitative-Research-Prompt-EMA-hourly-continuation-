# EMA Hourly Continuation — MEW/USDT P34_55

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 865 |
| net_profit_factor | 0.3776 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.6635 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -7.5253 |
| sortino_ratio | -3.1067 |
| max_drawdown | 0.9794 |
| cagr | -0.7857 |
| net_avg_win | 15.8821 |
| net_avg_loss | -32.0387 |
| avg_hold_time_bars | 3.0844 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
