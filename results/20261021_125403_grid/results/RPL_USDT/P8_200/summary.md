# EMA Hourly Continuation — RPL/USDT P8_200

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.9731 |
| net_win_rate | 0.5318 |
| gross_profit_factor | 1.1208 |
| gross_win_rate | 0.5318 |
| sharpe_ratio | -0.1004 |
| sortino_ratio | -0.0256 |
| max_drawdown | 0.2253 |
| cagr | -0.0173 |
| net_avg_win | 93.0826 |
| net_avg_loss | -108.6736 |
| avg_hold_time_bars | 56.9522 |
| exposure | 0.8093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
