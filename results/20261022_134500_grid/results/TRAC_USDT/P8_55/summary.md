# EMA Hourly Continuation — TRAC/USDT P8_55

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.5819 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -5.5939 |
| sortino_ratio | -2.4185 |
| max_drawdown | 0.9483 |
| cagr | -0.6857 |
| net_avg_win | 30.5257 |
| net_avg_loss | -43.9029 |
| avg_hold_time_bars | 10.8615 |
| exposure | 0.4670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
