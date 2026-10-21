# EMA Hourly Continuation — LPT/USDT P12_89

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7558 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.2753 |
| sortino_ratio | -0.7294 |
| max_drawdown | 0.6169 |
| cagr | -0.2862 |
| net_avg_win | 73.6622 |
| net_avg_loss | -87.2763 |
| avg_hold_time_bars | 24.4075 |
| exposure | 0.5636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
