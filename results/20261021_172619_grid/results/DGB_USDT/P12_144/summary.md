# EMA Hourly Continuation — DGB/USDT P12_144

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -1.9023 |
| sortino_ratio | -0.5677 |
| max_drawdown | 0.4997 |
| cagr | -0.2310 |
| net_avg_win | 69.3151 |
| net_avg_loss | -84.2868 |
| avg_hold_time_bars | 31.4932 |
| exposure | 0.6299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
