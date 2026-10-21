# EMA Hourly Continuation — WIF/USDT P26_34

**Symbol:** WIF/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.9570 |
| net_win_rate | 0.5507 |
| gross_profit_factor | 1.2196 |
| gross_win_rate | 0.5507 |
| sharpe_ratio | -0.1467 |
| sortino_ratio | -0.0250 |
| max_drawdown | 0.2304 |
| cagr | -0.0136 |
| net_avg_win | 99.1430 |
| net_avg_loss | -126.9909 |
| avg_hold_time_bars | 6.0725 |
| exposure | 0.0381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
