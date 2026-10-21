# EMA Hourly Continuation — BABYDOGE/USDT P50_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 27 |
| net_profit_factor | 1.5261 |
| net_win_rate | 0.6296 |
| gross_profit_factor | 1.6843 |
| gross_win_rate | 0.6296 |
| sharpe_ratio | 0.6919 |
| sortino_ratio | 0.0541 |
| max_drawdown | 0.0530 |
| cagr | 0.0222 |
| net_avg_win | 97.3695 |
| net_avg_loss | -108.4651 |
| avg_hold_time_bars | 16.6296 |
| exposure | 0.0203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
