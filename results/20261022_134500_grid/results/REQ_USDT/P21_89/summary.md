# EMA Hourly Continuation — REQ/USDT P21_89

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.5034 |
| net_win_rate | 0.4325 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -7.7794 |
| sortino_ratio | -3.1822 |
| max_drawdown | 0.9825 |
| cagr | -0.7978 |
| net_avg_win | 27.2660 |
| net_avg_loss | -41.2766 |
| avg_hold_time_bars | 10.1102 |
| exposure | 0.3879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
