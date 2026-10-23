# EMA Hourly Continuation — ERG/USDT P12_34

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1332 |
| net_profit_factor | 0.2880 |
| net_win_rate | 0.3386 |
| gross_profit_factor | 0.5633 |
| gross_win_rate | 0.3529 |
| sharpe_ratio | -14.0535 |
| sortino_ratio | -7.3286 |
| max_drawdown | 0.9999 |
| cagr | -0.9757 |
| net_avg_win | 8.9663 |
| net_avg_loss | -15.9397 |
| avg_hold_time_bars | 3.8904 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
