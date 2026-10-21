# EMA Hourly Continuation — NEO/USDT P8_34

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.6675 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9168 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -3.8930 |
| sortino_ratio | -1.5460 |
| max_drawdown | 0.8390 |
| cagr | -0.5063 |
| net_avg_win | 45.6512 |
| net_avg_loss | -61.3356 |
| avg_hold_time_bars | 8.5868 |
| exposure | 0.3013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
