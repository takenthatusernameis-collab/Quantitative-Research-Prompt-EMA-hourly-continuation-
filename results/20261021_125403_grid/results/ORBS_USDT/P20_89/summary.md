# EMA Hourly Continuation — ORBS/USDT P20_89

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9591 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -2.8917 |
| sortino_ratio | -0.9498 |
| max_drawdown | 0.6919 |
| cagr | -0.3535 |
| net_avg_win | 63.3099 |
| net_avg_loss | -82.3804 |
| avg_hold_time_bars | 17.4151 |
| exposure | 0.4195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
