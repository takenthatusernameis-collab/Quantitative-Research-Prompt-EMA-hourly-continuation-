# EMA Hourly Continuation — SKY/USDT P55_144

**Symbol:** SKY/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8984 |
| net_win_rate | 0.5434 |
| gross_profit_factor | 1.1836 |
| gross_win_rate | 0.5434 |
| sharpe_ratio | -0.6478 |
| sortino_ratio | -0.1831 |
| max_drawdown | 0.3469 |
| cagr | -0.0836 |
| net_avg_win | 85.6084 |
| net_avg_loss | -113.4102 |
| avg_hold_time_bars | 14.0354 |
| exposure | 0.2434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
