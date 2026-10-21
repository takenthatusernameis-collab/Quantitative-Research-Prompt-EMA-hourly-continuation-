# EMA Hourly Continuation — GMT/USDT P50_144

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7395 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9371 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.9194 |
| sortino_ratio | -0.5122 |
| max_drawdown | 0.5138 |
| cagr | -0.2098 |
| net_avg_win | 75.8835 |
| net_avg_loss | -93.6478 |
| avg_hold_time_bars | 15.4257 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
