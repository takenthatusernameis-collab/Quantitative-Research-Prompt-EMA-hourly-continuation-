# EMA Hourly Continuation — NEO/USDT P55_89

**Symbol:** NEO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.3298 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.7176 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -7.9897 |
| sortino_ratio | -3.0274 |
| max_drawdown | 0.9772 |
| cagr | -0.7758 |
| net_avg_win | 16.5147 |
| net_avg_loss | -35.2829 |
| avg_hold_time_bars | 3.9219 |
| exposure | 0.1255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
