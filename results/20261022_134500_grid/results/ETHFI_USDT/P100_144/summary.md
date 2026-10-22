# EMA Hourly Continuation — ETHFI/USDT P100_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.5485 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -4.2140 |
| sortino_ratio | -1.3654 |
| max_drawdown | 0.8102 |
| cagr | -0.4801 |
| net_avg_win | 39.6671 |
| net_avg_loss | -63.7975 |
| avg_hold_time_bars | 3.8008 |
| exposure | 0.0910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
