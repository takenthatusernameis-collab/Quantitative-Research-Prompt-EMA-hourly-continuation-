# EMA Hourly Continuation — LINK/USDT P12_20

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.6863 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.8958 |
| sortino_ratio | -0.4208 |
| max_drawdown | 0.4397 |
| cagr | -0.1752 |
| net_avg_win | 71.1230 |
| net_avg_loss | -101.0568 |
| avg_hold_time_bars | 5.2469 |
| exposure | 0.0570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
