# EMA Hourly Continuation — BDX/USDT P100_144

**Symbol:** BDX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.3585 |
| net_win_rate | 0.3842 |
| gross_profit_factor | 0.6340 |
| gross_win_rate | 0.3955 |
| sharpe_ratio | -3.8955 |
| sortino_ratio | -0.7472 |
| max_drawdown | 0.5804 |
| cagr | -0.2924 |
| net_avg_win | 47.7024 |
| net_avg_loss | -83.0088 |
| avg_hold_time_bars | 5.9209 |
| exposure | 0.0476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
