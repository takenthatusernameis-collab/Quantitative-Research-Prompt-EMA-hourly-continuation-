# EMA Hourly Continuation — ORBS/USDT P34_89

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.4945 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.9101 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -7.8580 |
| sortino_ratio | -3.0643 |
| max_drawdown | 0.9794 |
| cagr | -0.7831 |
| net_avg_win | 30.6842 |
| net_avg_loss | -42.9224 |
| avg_hold_time_bars | 7.7274 |
| exposure | 0.2680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
