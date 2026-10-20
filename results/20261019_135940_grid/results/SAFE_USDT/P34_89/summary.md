# EMA Hourly Continuation — SAFE/USDT P34_89

**Symbol:** SAFE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6399 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9971 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -3.6532 |
| sortino_ratio | -1.3139 |
| max_drawdown | 0.8100 |
| cagr | -0.4696 |
| net_avg_win | 44.5291 |
| net_avg_loss | -66.2392 |
| avg_hold_time_bars | 9.2077 |
| exposure | 0.2741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
