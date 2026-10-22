# EMA Hourly Continuation — FLR/USDT P50_100

**Symbol:** FLR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.3718 |
| net_win_rate | 0.4058 |
| gross_profit_factor | 0.7402 |
| gross_win_rate | 0.4216 |
| sharpe_ratio | -8.3902 |
| sortino_ratio | -3.2691 |
| max_drawdown | 0.9847 |
| cagr | -0.8090 |
| net_avg_win | 18.9164 |
| net_avg_loss | -34.7445 |
| avg_hold_time_bars | 4.9394 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
