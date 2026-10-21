# EMA Hourly Continuation — AUCTION/USDT P26_89

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.4214 |
| sortino_ratio | -1.1370 |
| max_drawdown | 0.7507 |
| cagr | -0.4122 |
| net_avg_win | 57.4197 |
| net_avg_loss | -76.2110 |
| avg_hold_time_bars | 12.4973 |
| exposure | 0.3117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
