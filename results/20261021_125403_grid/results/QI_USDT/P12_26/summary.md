# EMA Hourly Continuation — QI/USDT P12_26

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.5891 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.8689 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -4.1212 |
| sortino_ratio | -1.4974 |
| max_drawdown | 0.8252 |
| cagr | -0.4956 |
| net_avg_win | 38.6461 |
| net_avg_loss | -58.6749 |
| avg_hold_time_bars | 5.6920 |
| exposure | 0.1664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
