# EMA Hourly Continuation — NUM/USDT P55_200

**Symbol:** NUM/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6106 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8154 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.1274 |
| sortino_ratio | -0.8839 |
| max_drawdown | 0.6616 |
| cagr | -0.3425 |
| net_avg_win | 56.0989 |
| net_avg_loss | -74.3134 |
| avg_hold_time_bars | 21.3661 |
| exposure | 0.3953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
