# EMA Hourly Continuation — ERG/USDT P50_144

**Symbol:** ERG/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.3908 |
| net_win_rate | 0.3946 |
| gross_profit_factor | 0.6382 |
| gross_win_rate | 0.4018 |
| sharpe_ratio | -6.4139 |
| sortino_ratio | -2.1326 |
| max_drawdown | 0.9292 |
| cagr | -0.6494 |
| net_avg_win | 26.9362 |
| net_avg_loss | -44.9366 |
| avg_hold_time_bars | 10.6054 |
| exposure | 0.2700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
