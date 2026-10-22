# EMA Hourly Continuation — CSPR/USDT P12_89

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.7152 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8799 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.4693 |
| sortino_ratio | -0.8295 |
| max_drawdown | 0.6264 |
| cagr | -0.3175 |
| net_avg_win | 59.3329 |
| net_avg_loss | -72.9083 |
| avg_hold_time_bars | 17.0842 |
| exposure | 0.4333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
