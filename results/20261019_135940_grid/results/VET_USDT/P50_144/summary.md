# EMA Hourly Continuation — VET/USDT P50_144

**Symbol:** VET/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5808 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -3.4455 |
| sortino_ratio | -1.0933 |
| max_drawdown | 0.7548 |
| cagr | -0.4087 |
| net_avg_win | 40.9333 |
| net_avg_loss | -67.4838 |
| avg_hold_time_bars | 11.5641 |
| exposure | 0.2665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
