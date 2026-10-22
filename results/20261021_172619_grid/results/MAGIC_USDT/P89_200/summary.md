# EMA Hourly Continuation — MAGIC/USDT P89_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.6492 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8264 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -2.2523 |
| sortino_ratio | -0.5462 |
| max_drawdown | 0.4790 |
| cagr | -0.2230 |
| net_avg_win | 65.2863 |
| net_avg_loss | -84.6578 |
| avg_hold_time_bars | 16.2680 |
| exposure | 0.2152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
