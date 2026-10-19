# EMA Hourly Continuation — KMNO/USDT P8_34

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.9188 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -6.9685 |
| sortino_ratio | -3.3701 |
| max_drawdown | 0.9834 |
| cagr | -0.8087 |
| net_avg_win | 23.7834 |
| net_avg_loss | -35.7284 |
| avg_hold_time_bars | 5.9301 |
| exposure | 0.3212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
