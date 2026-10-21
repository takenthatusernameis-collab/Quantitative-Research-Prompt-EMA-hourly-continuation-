# EMA Hourly Continuation — TRX/USDT P89_200

**Symbol:** TRX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.4303 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -3.5676 |
| sortino_ratio | -0.7661 |
| max_drawdown | 0.5949 |
| cagr | -0.2998 |
| net_avg_win | 42.9449 |
| net_avg_loss | -88.7213 |
| avg_hold_time_bars | 15.0090 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
