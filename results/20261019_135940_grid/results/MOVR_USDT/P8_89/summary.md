# EMA Hourly Continuation — MOVR/USDT P8_89

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.5350 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8153 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -5.2503 |
| sortino_ratio | -2.0798 |
| max_drawdown | 0.9192 |
| cagr | -0.6272 |
| net_avg_win | 30.1148 |
| net_avg_loss | -44.4719 |
| avg_hold_time_bars | 17.6646 |
| exposure | 0.6367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
