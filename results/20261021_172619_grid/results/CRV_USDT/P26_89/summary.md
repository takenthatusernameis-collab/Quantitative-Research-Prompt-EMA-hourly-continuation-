# EMA Hourly Continuation — CRV/USDT P26_89

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.8808 |
| net_win_rate | 0.5232 |
| gross_profit_factor | 1.0948 |
| gross_win_rate | 0.5232 |
| sharpe_ratio | -0.8437 |
| sortino_ratio | -0.2587 |
| max_drawdown | 0.3113 |
| cagr | -0.1154 |
| net_avg_win | 82.6723 |
| net_avg_loss | -102.9831 |
| avg_hold_time_bars | 12.8852 |
| exposure | 0.2653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
