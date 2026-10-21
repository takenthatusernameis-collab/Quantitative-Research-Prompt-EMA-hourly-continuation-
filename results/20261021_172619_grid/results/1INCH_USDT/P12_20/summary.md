# EMA Hourly Continuation — 1INCH/USDT P12_20

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.5784 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.8873 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -3.1318 |
| sortino_ratio | -0.8464 |
| max_drawdown | 0.6258 |
| cagr | -0.3215 |
| net_avg_win | 50.5160 |
| net_avg_loss | -79.7909 |
| avg_hold_time_bars | 4.9237 |
| exposure | 0.0792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
