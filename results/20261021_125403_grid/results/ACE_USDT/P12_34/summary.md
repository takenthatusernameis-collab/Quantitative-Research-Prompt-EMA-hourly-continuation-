# EMA Hourly Continuation — ACE/USDT P12_34

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.9775 |
| sortino_ratio | -1.0737 |
| max_drawdown | 0.7111 |
| cagr | -0.3887 |
| net_avg_win | 51.0128 |
| net_avg_loss | -69.6793 |
| avg_hold_time_bars | 8.1674 |
| exposure | 0.2362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
