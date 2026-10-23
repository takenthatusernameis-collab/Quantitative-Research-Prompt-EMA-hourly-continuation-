# EMA Hourly Continuation — TFUEL/USDT P50_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.3984 |
| net_win_rate | 0.3934 |
| gross_profit_factor | 0.7604 |
| gross_win_rate | 0.4112 |
| sharpe_ratio | -8.7056 |
| sortino_ratio | -3.4564 |
| max_drawdown | 0.9865 |
| cagr | -0.8176 |
| net_avg_win | 21.2107 |
| net_avg_loss | -34.5183 |
| avg_hold_time_bars | 4.6986 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
