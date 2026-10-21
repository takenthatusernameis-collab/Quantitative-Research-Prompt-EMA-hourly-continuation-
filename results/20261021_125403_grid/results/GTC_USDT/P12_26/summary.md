# EMA Hourly Continuation — GTC/USDT P12_26

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.6379 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -3.5410 |
| sortino_ratio | -1.2119 |
| max_drawdown | 0.7574 |
| cagr | -0.4257 |
| net_avg_win | 49.0443 |
| net_avg_loss | -68.5071 |
| avg_hold_time_bars | 5.6719 |
| exposure | 0.1477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
