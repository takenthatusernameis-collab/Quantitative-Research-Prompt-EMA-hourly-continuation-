# EMA Hourly Continuation — ZIL/USDT P20_34

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6859 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0239 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -2.2501 |
| sortino_ratio | -0.6075 |
| max_drawdown | 0.5331 |
| cagr | -0.2417 |
| net_avg_win | 61.7760 |
| net_avg_loss | -91.6216 |
| avg_hold_time_bars | 5.1937 |
| exposure | 0.0829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
