# EMA Hourly Continuation — TRAC/USDT P26_200

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7648 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9074 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -1.5476 |
| sortino_ratio | -0.3918 |
| max_drawdown | 0.4035 |
| cagr | -0.1656 |
| net_avg_win | 79.2212 |
| net_avg_loss | -93.0351 |
| avg_hold_time_bars | 38.4669 |
| exposure | 0.5543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
