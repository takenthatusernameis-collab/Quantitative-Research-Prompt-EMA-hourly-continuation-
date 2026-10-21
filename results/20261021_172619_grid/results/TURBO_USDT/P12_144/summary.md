# EMA Hourly Continuation — TURBO/USDT P12_144

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8647 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.0170 |
| sortino_ratio | -0.2971 |
| max_drawdown | 0.3946 |
| cagr | -0.1307 |
| net_avg_win | 92.8065 |
| net_avg_loss | -108.5647 |
| avg_hold_time_bars | 32.7040 |
| exposure | 0.6209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
