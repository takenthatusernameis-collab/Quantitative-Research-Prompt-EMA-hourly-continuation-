# EMA Hourly Continuation — RIO/USDT P55_144

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7270 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -1.8169 |
| sortino_ratio | -0.4797 |
| max_drawdown | 0.4691 |
| cagr | -0.1989 |
| net_avg_win | 71.9006 |
| net_avg_loss | -83.0355 |
| avg_hold_time_bars | 13.1541 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
