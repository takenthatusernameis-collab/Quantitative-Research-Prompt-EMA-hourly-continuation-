# EMA Hourly Continuation — DODO/USDT P8_144

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6936 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -2.5787 |
| sortino_ratio | -0.7805 |
| max_drawdown | 0.6138 |
| cagr | -0.3020 |
| net_avg_win | 65.2010 |
| net_avg_loss | -77.2183 |
| avg_hold_time_bars | 32.5468 |
| exposure | 0.6760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
