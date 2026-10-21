# EMA Hourly Continuation — ONT/USDT P12_144

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8486 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.2258 |
| sortino_ratio | -0.6451 |
| max_drawdown | 0.5583 |
| cagr | -0.2577 |
| net_avg_win | 65.5055 |
| net_avg_loss | -78.9755 |
| avg_hold_time_bars | 32.4357 |
| exposure | 0.6165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
