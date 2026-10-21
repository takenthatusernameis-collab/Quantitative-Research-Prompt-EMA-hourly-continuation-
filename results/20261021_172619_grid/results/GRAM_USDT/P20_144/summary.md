# EMA Hourly Continuation — GRAM/USDT P20_144

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7025 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -2.0614 |
| sortino_ratio | -0.5732 |
| max_drawdown | 0.5184 |
| cagr | -0.2314 |
| net_avg_win | 62.4050 |
| net_avg_loss | -82.5159 |
| avg_hold_time_bars | 27.8816 |
| exposure | 0.4816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
