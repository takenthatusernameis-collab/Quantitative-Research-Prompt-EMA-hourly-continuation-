# EMA Hourly Continuation — UQC/USDT P12_89

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.3406 |
| net_win_rate | 0.2791 |
| gross_profit_factor | 0.5642 |
| gross_win_rate | 0.3282 |
| sharpe_ratio | -7.8681 |
| sortino_ratio | -2.0182 |
| max_drawdown | 0.9426 |
| cagr | -0.6780 |
| net_avg_win | 53.5046 |
| net_avg_loss | -60.8299 |
| avg_hold_time_bars | 42.6319 |
| exposure | 0.6290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
