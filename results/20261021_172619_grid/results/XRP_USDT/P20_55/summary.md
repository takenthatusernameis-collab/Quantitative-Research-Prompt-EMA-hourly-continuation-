# EMA Hourly Continuation — XRP/USDT P20_55

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6372 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9652 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -3.1163 |
| sortino_ratio | -0.9626 |
| max_drawdown | 0.6838 |
| cagr | -0.3565 |
| net_avg_win | 52.4852 |
| net_avg_loss | -76.8799 |
| avg_hold_time_bars | 8.7629 |
| exposure | 0.1848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
