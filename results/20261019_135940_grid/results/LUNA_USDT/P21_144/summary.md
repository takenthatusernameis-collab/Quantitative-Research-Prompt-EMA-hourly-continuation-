# EMA Hourly Continuation — LUNA/USDT P21_144

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5646 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -5.1769 |
| sortino_ratio | -1.8235 |
| max_drawdown | 0.8933 |
| cagr | -0.5888 |
| net_avg_win | 41.2009 |
| net_avg_loss | -58.9200 |
| avg_hold_time_bars | 16.5962 |
| exposure | 0.4745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
