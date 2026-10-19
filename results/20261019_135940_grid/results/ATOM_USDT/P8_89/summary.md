# EMA Hourly Continuation — ATOM/USDT P8_89

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.6211 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0166 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -3.3119 |
| sortino_ratio | -1.0751 |
| max_drawdown | 0.7453 |
| cagr | -0.4089 |
| net_avg_win | 44.8316 |
| net_avg_loss | -70.8605 |
| avg_hold_time_bars | 29.0203 |
| exposure | 0.7136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
