# EMA Hourly Continuation — YGG/USDT P100_200

**Symbol:** YGG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.8187 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0208 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -0.9755 |
| sortino_ratio | -0.2325 |
| max_drawdown | 0.2697 |
| cagr | -0.1027 |
| net_avg_win | 76.5868 |
| net_avg_loss | -96.9910 |
| avg_hold_time_bars | 12.3935 |
| exposure | 0.1553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
