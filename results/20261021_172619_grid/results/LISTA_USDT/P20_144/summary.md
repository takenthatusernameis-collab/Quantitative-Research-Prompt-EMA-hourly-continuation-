# EMA Hourly Continuation — LISTA/USDT P20_144

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.8511 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0272 |
| sortino_ratio | -0.2923 |
| max_drawdown | 0.3304 |
| cagr | -0.1283 |
| net_avg_win | 85.1576 |
| net_avg_loss | -100.0587 |
| avg_hold_time_bars | 28.7799 |
| exposure | 0.5179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
