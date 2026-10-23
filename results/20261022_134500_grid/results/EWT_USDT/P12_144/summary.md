# EMA Hourly Continuation — EWT/USDT P12_144

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.5192 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.7443 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -4.7300 |
| sortino_ratio | -1.6423 |
| max_drawdown | 0.8789 |
| cagr | -0.5462 |
| net_avg_win | 34.8828 |
| net_avg_loss | -51.4008 |
| avg_hold_time_bars | 19.0747 |
| exposure | 0.5341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
