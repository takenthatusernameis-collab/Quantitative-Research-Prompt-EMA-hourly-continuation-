# EMA Hourly Continuation — ATOM/USDT P8_200

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.8534 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -0.7158 |
| sortino_ratio | -0.1502 |
| max_drawdown | 0.2353 |
| cagr | -0.0680 |
| net_avg_win | 87.3312 |
| net_avg_loss | -104.2673 |
| avg_hold_time_bars | 87.5794 |
| exposure | 0.8519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
