# EMA Hourly Continuation — TAO/USDT P55_100

**Symbol:** TAO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9030 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -4.1737 |
| sortino_ratio | -1.4227 |
| max_drawdown | 0.8268 |
| cagr | -0.5026 |
| net_avg_win | 33.7188 |
| net_avg_loss | -59.5867 |
| avg_hold_time_bars | 5.0352 |
| exposure | 0.1364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
