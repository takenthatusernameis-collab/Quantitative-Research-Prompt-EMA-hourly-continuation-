# EMA Hourly Continuation — BTT/USDT P8_144

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.4930 |
| net_win_rate | 0.4359 |
| gross_profit_factor | 0.8625 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -4.1317 |
| sortino_ratio | -1.0871 |
| max_drawdown | 0.7529 |
| cagr | -0.4111 |
| net_avg_win | 46.7530 |
| net_avg_loss | -73.2733 |
| avg_hold_time_bars | 50.3818 |
| exposure | 0.8038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
