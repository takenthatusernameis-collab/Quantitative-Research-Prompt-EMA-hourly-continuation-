# EMA Hourly Continuation — SAFE/USDT P8_144

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7682 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -1.5732 |
| sortino_ratio | -0.4544 |
| max_drawdown | 0.4263 |
| cagr | -0.1906 |
| net_avg_win | 68.9075 |
| net_avg_loss | -83.3578 |
| avg_hold_time_bars | 38.2176 |
| exposure | 0.7158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
