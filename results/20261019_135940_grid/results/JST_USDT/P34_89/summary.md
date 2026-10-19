# EMA Hourly Continuation — JST/USDT P34_89

**Symbol:** JST/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.3342 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.9731 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -6.8868 |
| sortino_ratio | -2.4359 |
| max_drawdown | 0.9577 |
| cagr | -0.7124 |
| net_avg_win | 16.9721 |
| net_avg_loss | -41.4172 |
| avg_hold_time_bars | 8.1317 |
| exposure | 0.2318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
