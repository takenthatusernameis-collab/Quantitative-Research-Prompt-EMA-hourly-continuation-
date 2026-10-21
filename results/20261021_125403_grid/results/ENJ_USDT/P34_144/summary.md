# EMA Hourly Continuation — ENJ/USDT P34_144

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.8571 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0509 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -0.9052 |
| sortino_ratio | -0.2456 |
| max_drawdown | 0.3522 |
| cagr | -0.1093 |
| net_avg_win | 82.4952 |
| net_avg_loss | -101.2040 |
| avg_hold_time_bars | 26.8524 |
| exposure | 0.4362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
