# EMA Hourly Continuation — SYN/USDT P8_89

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6979 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -3.2543 |
| sortino_ratio | -1.2328 |
| max_drawdown | 0.7724 |
| cagr | -0.4427 |
| net_avg_win | 51.3770 |
| net_avg_loss | -68.2916 |
| avg_hold_time_bars | 19.5132 |
| exposure | 0.6377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
