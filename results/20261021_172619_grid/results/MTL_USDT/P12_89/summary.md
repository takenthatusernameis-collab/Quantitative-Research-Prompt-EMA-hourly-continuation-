# EMA Hourly Continuation — MTL/USDT P12_89

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6989 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.6971 |
| sortino_ratio | -0.8099 |
| max_drawdown | 0.6388 |
| cagr | -0.3134 |
| net_avg_win | 67.3987 |
| net_avg_loss | -85.8532 |
| avg_hold_time_bars | 31.1830 |
| exposure | 0.6322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
