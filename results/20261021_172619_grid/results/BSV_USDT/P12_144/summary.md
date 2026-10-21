# EMA Hourly Continuation — BSV/USDT P12_144

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5940 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.7432 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -3.2061 |
| sortino_ratio | -0.9092 |
| max_drawdown | 0.6575 |
| cagr | -0.3421 |
| net_avg_win | 55.0224 |
| net_avg_loss | -69.3700 |
| avg_hold_time_bars | 37.0050 |
| exposure | 0.6795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
