# EMA Hourly Continuation — ENJ/USDT P100_144

**Symbol:** ENJ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.9119 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -4.9796 |
| sortino_ratio | -1.5356 |
| max_drawdown | 0.8508 |
| cagr | -0.5262 |
| net_avg_win | 37.8989 |
| net_avg_loss | -64.8924 |
| avg_hold_time_bars | 4.5294 |
| exposure | 0.0976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
