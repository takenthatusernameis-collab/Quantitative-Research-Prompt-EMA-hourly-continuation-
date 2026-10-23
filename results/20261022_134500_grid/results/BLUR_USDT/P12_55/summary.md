# EMA Hourly Continuation — BLUR/USDT P12_55

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.6229 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -5.3119 |
| sortino_ratio | -2.3254 |
| max_drawdown | 0.9431 |
| cagr | -0.6732 |
| net_avg_win | 34.0633 |
| net_avg_loss | -48.2351 |
| avg_hold_time_bars | 8.5725 |
| exposure | 0.3774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
