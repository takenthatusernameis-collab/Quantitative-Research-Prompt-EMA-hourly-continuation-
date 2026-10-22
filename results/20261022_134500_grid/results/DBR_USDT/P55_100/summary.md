# EMA Hourly Continuation — DBR/USDT P55_100

**Symbol:** DBR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.4141 |
| net_win_rate | 0.4093 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -6.7353 |
| sortino_ratio | -2.1911 |
| max_drawdown | 0.8993 |
| cagr | -0.6727 |
| net_avg_win | 35.8953 |
| net_avg_loss | -60.0586 |
| avg_hold_time_bars | 6.6023 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
