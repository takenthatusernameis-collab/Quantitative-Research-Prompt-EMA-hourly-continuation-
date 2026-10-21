# EMA Hourly Continuation — KSM/USDT P12_34

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6714 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -3.1621 |
| sortino_ratio | -1.1474 |
| max_drawdown | 0.7493 |
| cagr | -0.4081 |
| net_avg_win | 47.9437 |
| net_avg_loss | -67.5110 |
| avg_hold_time_bars | 6.9486 |
| exposure | 0.2028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
