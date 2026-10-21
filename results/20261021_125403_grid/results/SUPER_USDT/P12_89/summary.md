# EMA Hourly Continuation — SUPER/USDT P12_89

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.8404 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0287 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.2846 |
| sortino_ratio | -0.4344 |
| max_drawdown | 0.4647 |
| cagr | -0.1833 |
| net_avg_win | 74.1755 |
| net_avg_loss | -91.4928 |
| avg_hold_time_bars | 20.4730 |
| exposure | 0.5174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
