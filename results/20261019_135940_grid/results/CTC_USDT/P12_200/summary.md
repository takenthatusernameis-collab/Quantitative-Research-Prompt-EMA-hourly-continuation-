# EMA Hourly Continuation — CTC/USDT P12_200

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -3.5536 |
| sortino_ratio | -1.0770 |
| max_drawdown | 0.7599 |
| cagr | -0.4125 |
| net_avg_win | 51.9137 |
| net_avg_loss | -73.6931 |
| avg_hold_time_bars | 32.6421 |
| exposure | 0.7048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
