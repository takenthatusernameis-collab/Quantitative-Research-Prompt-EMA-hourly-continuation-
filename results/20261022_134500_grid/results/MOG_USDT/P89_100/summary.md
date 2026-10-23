# EMA Hourly Continuation — MOG/USDT P89_100

**Symbol:** MOG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.4324 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8049 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -6.6830 |
| sortino_ratio | -2.2478 |
| max_drawdown | 0.9275 |
| cagr | -0.6806 |
| net_avg_win | 31.2538 |
| net_avg_loss | -55.3765 |
| avg_hold_time_bars | 2.2764 |
| exposure | 0.0590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
