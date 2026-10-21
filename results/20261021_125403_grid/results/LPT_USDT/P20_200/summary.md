# EMA Hourly Continuation — LPT/USDT P20_200

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -1.9287 |
| sortino_ratio | -0.5104 |
| max_drawdown | 0.5000 |
| cagr | -0.2094 |
| net_avg_win | 69.6443 |
| net_avg_loss | -83.7977 |
| avg_hold_time_bars | 37.4943 |
| exposure | 0.5931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
