# EMA Hourly Continuation — FLR/USDT P12_200

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8745 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.0961 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.7571 |
| sortino_ratio | -0.2255 |
| max_drawdown | 0.2781 |
| cagr | -0.1018 |
| net_avg_win | 72.8875 |
| net_avg_loss | -93.2503 |
| avg_hold_time_bars | 33.4463 |
| exposure | 0.6507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
