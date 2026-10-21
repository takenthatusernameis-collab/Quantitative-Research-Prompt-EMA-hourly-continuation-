# EMA Hourly Continuation — WEMIX/USDT P8_50

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.5702 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.7314 |
| gross_win_rate | 0.4150 |
| sharpe_ratio | -4.6539 |
| sortino_ratio | -1.5970 |
| max_drawdown | 0.8476 |
| cagr | -0.5224 |
| net_avg_win | 45.8725 |
| net_avg_loss | -57.0628 |
| avg_hold_time_bars | 14.4881 |
| exposure | 0.3872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
