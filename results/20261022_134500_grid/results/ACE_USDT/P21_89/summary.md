# EMA Hourly Continuation — ACE/USDT P21_89

**Symbol:** ACE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.7419 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0510 |
| gross_win_rate | 0.5137 |
| sharpe_ratio | -2.2305 |
| sortino_ratio | -0.7691 |
| max_drawdown | 0.6268 |
| cagr | -0.2987 |
| net_avg_win | 57.2503 |
| net_avg_loss | -79.2981 |
| avg_hold_time_bars | 14.4300 |
| exposure | 0.3827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
