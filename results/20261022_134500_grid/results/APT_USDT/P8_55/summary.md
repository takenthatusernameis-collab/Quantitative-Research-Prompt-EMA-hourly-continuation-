# EMA Hourly Continuation — APT/USDT P8_55

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.5603 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -5.4803 |
| sortino_ratio | -2.4040 |
| max_drawdown | 0.9512 |
| cagr | -0.6904 |
| net_avg_win | 26.1267 |
| net_avg_loss | -41.4309 |
| avg_hold_time_bars | 11.2831 |
| exposure | 0.5036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
