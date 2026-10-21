# EMA Hourly Continuation — FLOW/USDT P26_89

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7174 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9264 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -2.2417 |
| sortino_ratio | -0.7001 |
| max_drawdown | 0.5676 |
| cagr | -0.2751 |
| net_avg_win | 60.9152 |
| net_avg_loss | -79.0886 |
| avg_hold_time_bars | 13.1169 |
| exposure | 0.2856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
