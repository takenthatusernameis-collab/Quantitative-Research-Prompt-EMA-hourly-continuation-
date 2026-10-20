# EMA Hourly Continuation — AGLD/USDT P89_200

**Symbol:** AGLD/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.6480 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9269 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -2.8969 |
| sortino_ratio | -0.8203 |
| max_drawdown | 0.6331 |
| cagr | -0.3203 |
| net_avg_win | 60.3147 |
| net_avg_loss | -82.2529 |
| avg_hold_time_bars | 11.9556 |
| exposure | 0.2191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
