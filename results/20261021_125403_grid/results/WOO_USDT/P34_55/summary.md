# EMA Hourly Continuation — WOO/USDT P34_55

**Symbol:** WOO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9372 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.4781 |
| sortino_ratio | -0.7087 |
| max_drawdown | 0.5756 |
| cagr | -0.2771 |
| net_avg_win | 63.1654 |
| net_avg_loss | -85.5100 |
| avg_hold_time_bars | 6.0326 |
| exposure | 0.1094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
