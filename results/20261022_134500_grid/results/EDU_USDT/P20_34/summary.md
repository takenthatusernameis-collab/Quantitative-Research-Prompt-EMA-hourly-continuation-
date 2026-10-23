# EMA Hourly Continuation — EDU/USDT P20_34

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.3798 |
| net_win_rate | 0.4109 |
| gross_profit_factor | 0.7342 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -9.7448 |
| sortino_ratio | -4.7225 |
| max_drawdown | 0.9971 |
| cagr | -0.9011 |
| net_avg_win | 12.6674 |
| net_avg_loss | -23.2655 |
| avg_hold_time_bars | 3.1654 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
