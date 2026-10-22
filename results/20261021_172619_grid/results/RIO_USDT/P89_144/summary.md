# EMA Hourly Continuation — RIO/USDT P89_144

**Symbol:** RIO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.7215 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8504 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -1.5821 |
| sortino_ratio | -0.3503 |
| max_drawdown | 0.3470 |
| cagr | -0.1492 |
| net_avg_win | 77.2305 |
| net_avg_loss | -91.3915 |
| avg_hold_time_bars | 7.6971 |
| exposure | 0.0852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
