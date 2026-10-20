# EMA Hourly Continuation — ARPA/USDT P55_144

**Symbol:** ARPA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.4845 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.7861 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -5.1637 |
| sortino_ratio | -1.7316 |
| max_drawdown | 0.8771 |
| cagr | -0.5628 |
| net_avg_win | 33.3246 |
| net_avg_loss | -53.0954 |
| avg_hold_time_bars | 10.5132 |
| exposure | 0.2697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
