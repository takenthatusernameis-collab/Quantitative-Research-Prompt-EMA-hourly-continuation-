# EMA Hourly Continuation — REQ/USDT P55_89

**Symbol:** REQ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.5400 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -4.3695 |
| sortino_ratio | -1.1871 |
| max_drawdown | 0.7538 |
| cagr | -0.4234 |
| net_avg_win | 56.3715 |
| net_avg_loss | -80.6189 |
| avg_hold_time_bars | 6.7179 |
| exposure | 0.1093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
