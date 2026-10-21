# EMA Hourly Continuation — AMP/USDT P12_55

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.4820 |
| net_win_rate | 0.3933 |
| gross_profit_factor | 0.6473 |
| gross_win_rate | 0.3933 |
| sharpe_ratio | -6.1547 |
| sortino_ratio | -2.3327 |
| max_drawdown | 0.9350 |
| cagr | -0.6608 |
| net_avg_win | 30.8073 |
| net_avg_loss | -41.4381 |
| avg_hold_time_bars | 10.0209 |
| exposure | 0.3266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
