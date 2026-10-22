# EMA Hourly Continuation — ETHFI/USDT P26_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9681 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -3.6926 |
| sortino_ratio | -1.3932 |
| max_drawdown | 0.8165 |
| cagr | -0.4858 |
| net_avg_win | 48.7640 |
| net_avg_loss | -66.4280 |
| avg_hold_time_bars | 11.1046 |
| exposure | 0.3619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
