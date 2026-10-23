# EMA Hourly Continuation — MTL/USDT P12_20

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1377 |
| net_profit_factor | 0.3141 |
| net_win_rate | 0.3878 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -13.6069 |
| sortino_ratio | -7.2647 |
| max_drawdown | 0.9999 |
| cagr | -0.9756 |
| net_avg_win | 8.5739 |
| net_avg_loss | -17.2926 |
| avg_hold_time_bars | 3.1206 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
