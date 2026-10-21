# EMA Hourly Continuation — QNT/USDT P20_144

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0347 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.5087 |
| sortino_ratio | -0.4644 |
| max_drawdown | 0.4784 |
| cagr | -0.1927 |
| net_avg_win | 76.3423 |
| net_avg_loss | -96.6789 |
| avg_hold_time_bars | 23.8870 |
| exposure | 0.4995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
