# EMA Hourly Continuation — DEGEN/USDT P20_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.7284 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9965 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -3.1653 |
| sortino_ratio | -1.1846 |
| max_drawdown | 0.7774 |
| cagr | -0.4331 |
| net_avg_win | 59.0112 |
| net_avg_loss | -77.2063 |
| avg_hold_time_bars | 12.1047 |
| exposure | 0.3896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
