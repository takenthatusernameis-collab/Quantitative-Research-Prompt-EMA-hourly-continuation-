# EMA Hourly Continuation — APT/USDT P8_55

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.8193 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -1.4340 |
| sortino_ratio | -0.5121 |
| max_drawdown | 0.4869 |
| cagr | -0.2120 |
| net_avg_win | 64.8174 |
| net_avg_loss | -81.9761 |
| avg_hold_time_bars | 16.8724 |
| exposure | 0.4747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
