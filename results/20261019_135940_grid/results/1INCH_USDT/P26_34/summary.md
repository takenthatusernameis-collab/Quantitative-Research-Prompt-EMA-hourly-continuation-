# EMA Hourly Continuation — 1INCH/USDT P26_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.2536 |
| net_win_rate | 0.3695 |
| gross_profit_factor | 0.7308 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -14.0274 |
| sortino_ratio | -7.0481 |
| max_drawdown | 0.9999 |
| cagr | -0.9745 |
| net_avg_win | 7.7392 |
| net_avg_loss | -17.8858 |
| avg_hold_time_bars | 2.0842 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
