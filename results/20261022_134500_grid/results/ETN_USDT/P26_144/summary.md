# EMA Hourly Continuation — ETN/USDT P26_144

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.4681 |
| net_win_rate | 0.3946 |
| gross_profit_factor | 0.6808 |
| gross_win_rate | 0.4018 |
| sharpe_ratio | -6.7347 |
| sortino_ratio | -2.4464 |
| max_drawdown | 0.9198 |
| cagr | -0.6948 |
| net_avg_win | 36.5293 |
| net_avg_loss | -50.8761 |
| avg_hold_time_bars | 13.6000 |
| exposure | 0.4137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
