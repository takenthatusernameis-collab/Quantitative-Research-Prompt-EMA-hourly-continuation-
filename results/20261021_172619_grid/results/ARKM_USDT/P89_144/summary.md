# EMA Hourly Continuation — ARKM/USDT P89_144

**Symbol:** ARKM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.6496 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8237 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -2.1245 |
| sortino_ratio | -0.4994 |
| max_drawdown | 0.4482 |
| cagr | -0.2047 |
| net_avg_win | 64.8760 |
| net_avg_loss | -84.3492 |
| avg_hold_time_bars | 8.3810 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
