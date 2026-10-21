# EMA Hourly Continuation — AR/USDT P20_144

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7409 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8684 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -1.7368 |
| sortino_ratio | -0.4662 |
| max_drawdown | 0.4388 |
| cagr | -0.1940 |
| net_avg_win | 71.5965 |
| net_avg_loss | -84.9396 |
| avg_hold_time_bars | 34.4370 |
| exposure | 0.5588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
