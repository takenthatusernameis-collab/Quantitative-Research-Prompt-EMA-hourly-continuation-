# EMA Hourly Continuation — FLUX/USDT P26_89

**Symbol:** FLUX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7181 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -2.2219 |
| sortino_ratio | -0.6957 |
| max_drawdown | 0.5752 |
| cagr | -0.2736 |
| net_avg_win | 60.8684 |
| net_avg_loss | -78.3204 |
| avg_hold_time_bars | 12.5281 |
| exposure | 0.2739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
