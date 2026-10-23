# EMA Hourly Continuation — POKT/USDT P20_100

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.6028 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.8899 |
| gross_win_rate | 0.4274 |
| sharpe_ratio | -6.2076 |
| sortino_ratio | -2.5483 |
| max_drawdown | 0.9547 |
| cagr | -0.7025 |
| net_avg_win | 40.2796 |
| net_avg_loss | -48.4657 |
| avg_hold_time_bars | 10.7494 |
| exposure | 0.4154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
