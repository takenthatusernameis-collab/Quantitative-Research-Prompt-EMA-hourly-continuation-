# EMA Hourly Continuation — BIGTIME/USDT P12_50

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.7835 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 0.9965 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -1.9816 |
| sortino_ratio | -0.7364 |
| max_drawdown | 0.5942 |
| cagr | -0.2877 |
| net_avg_win | 61.2196 |
| net_avg_loss | -79.2991 |
| avg_hold_time_bars | 10.4415 |
| exposure | 0.3189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
