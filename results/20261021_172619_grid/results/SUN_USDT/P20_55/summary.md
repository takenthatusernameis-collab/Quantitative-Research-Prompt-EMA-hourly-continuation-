# EMA Hourly Continuation — SUN/USDT P20_55

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.4795 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.8404 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -6.3261 |
| sortino_ratio | -2.0797 |
| max_drawdown | 0.9187 |
| cagr | -0.6302 |
| net_avg_win | 38.1271 |
| net_avg_loss | -57.4948 |
| avg_hold_time_bars | 11.0454 |
| exposure | 0.2644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
