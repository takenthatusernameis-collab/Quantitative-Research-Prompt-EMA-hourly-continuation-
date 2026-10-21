# EMA Hourly Continuation — DGB/USDT P100_144

**Symbol:** DGB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.6149 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8411 |
| gross_win_rate | 0.4506 |
| sharpe_ratio | -2.4237 |
| sortino_ratio | -0.5276 |
| max_drawdown | 0.4762 |
| cagr | -0.2154 |
| net_avg_win | 69.3745 |
| net_avg_loss | -92.5489 |
| avg_hold_time_bars | 6.2876 |
| exposure | 0.0666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
