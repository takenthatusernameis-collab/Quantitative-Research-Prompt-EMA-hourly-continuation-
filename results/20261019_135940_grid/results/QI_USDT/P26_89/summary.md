# EMA Hourly Continuation — QI/USDT P26_89

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.6366 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 1.0454 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -3.5693 |
| sortino_ratio | -1.2861 |
| max_drawdown | 0.7950 |
| cagr | -0.4568 |
| net_avg_win | 42.3382 |
| net_avg_loss | -66.7142 |
| avg_hold_time_bars | 10.4777 |
| exposure | 0.3077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
