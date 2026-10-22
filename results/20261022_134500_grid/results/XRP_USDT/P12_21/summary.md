# EMA Hourly Continuation — XRP/USDT P12_21

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1443 |
| net_profit_factor | 0.1455 |
| net_win_rate | 0.3611 |
| gross_profit_factor | 0.6490 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -16.5733 |
| sortino_ratio | -9.1891 |
| max_drawdown | 1.0000 |
| cagr | -0.9938 |
| net_avg_win | 3.2682 |
| net_avg_loss | -12.6927 |
| avg_hold_time_bars | 2.2079 |
| exposure | 0.1448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
