# EMA Hourly Continuation — TAO/USDT P12_144

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.7409 |
| sortino_ratio | -0.8726 |
| max_drawdown | 0.6705 |
| cagr | -0.3435 |
| net_avg_win | 61.2585 |
| net_avg_loss | -80.7290 |
| avg_hold_time_bars | 27.8259 |
| exposure | 0.6539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
