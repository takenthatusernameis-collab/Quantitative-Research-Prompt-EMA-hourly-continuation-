# EMA Hourly Continuation — CRO/USDT P89_144

**Symbol:** CRO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.3326 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.7603 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -6.6652 |
| sortino_ratio | -2.0967 |
| max_drawdown | 0.9335 |
| cagr | -0.6580 |
| net_avg_win | 22.1253 |
| net_avg_loss | -49.1917 |
| avg_hold_time_bars | 5.3968 |
| exposure | 0.1212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
