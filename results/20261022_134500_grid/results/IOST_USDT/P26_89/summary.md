# EMA Hourly Continuation — IOST/USDT P26_89

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.5864 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 1.0130 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -4.0853 |
| sortino_ratio | -1.4867 |
| max_drawdown | 0.8400 |
| cagr | -0.5115 |
| net_avg_win | 35.8474 |
| net_avg_loss | -60.2237 |
| avg_hold_time_bars | 11.3654 |
| exposure | 0.3435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
