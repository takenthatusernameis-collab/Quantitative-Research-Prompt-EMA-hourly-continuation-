# EMA Hourly Continuation — WEMIX/USDT P26_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1103 |
| net_profit_factor | 0.2421 |
| net_win_rate | 0.2829 |
| gross_profit_factor | 0.4391 |
| gross_win_rate | 0.2956 |
| sharpe_ratio | -14.5694 |
| sortino_ratio | -6.9530 |
| max_drawdown | 0.9999 |
| cagr | -0.9715 |
| net_avg_win | 10.2386 |
| net_avg_loss | -16.6790 |
| avg_hold_time_bars | 7.6029 |
| exposure | 0.3812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
