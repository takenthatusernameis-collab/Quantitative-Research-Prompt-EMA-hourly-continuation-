# EMA Hourly Continuation — TAO/USDT P55_100

**Symbol:** TAO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.8600 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0709 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -0.7387 |
| sortino_ratio | -0.1818 |
| max_drawdown | 0.2083 |
| cagr | -0.0822 |
| net_avg_win | 78.2966 |
| net_avg_loss | -98.8442 |
| avg_hold_time_bars | 8.3253 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
