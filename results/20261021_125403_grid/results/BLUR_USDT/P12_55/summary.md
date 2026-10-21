# EMA Hourly Continuation — BLUR/USDT P12_55

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.8077 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0362 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.8622 |
| sortino_ratio | -0.6822 |
| max_drawdown | 0.6025 |
| cagr | -0.2706 |
| net_avg_win | 69.4632 |
| net_avg_loss | -88.1203 |
| avg_hold_time_bars | 11.7713 |
| exposure | 0.3494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
