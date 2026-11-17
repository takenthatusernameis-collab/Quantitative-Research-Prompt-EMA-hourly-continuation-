# EMA Hourly Continuation — NUM/USDT P26_50

**Symbol:** NUM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.3421 |
| net_win_rate | 0.3392 |
| gross_profit_factor | 0.7289 |
| gross_win_rate | 0.3580 |
| sharpe_ratio | -11.3883 |
| sortino_ratio | -5.0169 |
| max_drawdown | 0.9983 |
| cagr | -0.9201 |
| net_avg_win | 15.9210 |
| net_avg_loss | -23.8941 |
| avg_hold_time_bars | 4.4152 |
| exposure | 0.1929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
