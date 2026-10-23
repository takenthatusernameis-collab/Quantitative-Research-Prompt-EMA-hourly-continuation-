# EMA Hourly Continuation — SATS/USDT P21_55

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 865 |
| net_profit_factor | 0.5580 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8896 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -5.9199 |
| sortino_ratio | -2.4493 |
| max_drawdown | 0.9487 |
| cagr | -0.6891 |
| net_avg_win | 31.3180 |
| net_avg_loss | -44.3862 |
| avg_hold_time_bars | 5.7468 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
