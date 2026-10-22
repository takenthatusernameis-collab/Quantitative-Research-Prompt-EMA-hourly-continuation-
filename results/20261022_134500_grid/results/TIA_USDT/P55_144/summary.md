# EMA Hourly Continuation — TIA/USDT P55_144

**Symbol:** TIA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6248 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8938 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -3.3189 |
| sortino_ratio | -0.9964 |
| max_drawdown | 0.7073 |
| cagr | -0.3835 |
| net_avg_win | 54.4620 |
| net_avg_loss | -76.4973 |
| avg_hold_time_bars | 11.8978 |
| exposure | 0.2488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
