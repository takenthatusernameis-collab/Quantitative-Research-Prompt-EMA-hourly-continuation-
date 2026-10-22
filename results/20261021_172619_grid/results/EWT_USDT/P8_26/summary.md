# EMA Hourly Continuation — EWT/USDT P8_26

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.5653 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.7580 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -4.3568 |
| sortino_ratio | -1.4280 |
| max_drawdown | 0.8185 |
| cagr | -0.4838 |
| net_avg_win | 46.4067 |
| net_avg_loss | -60.6974 |
| avg_hold_time_bars | 7.2116 |
| exposure | 0.1750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
