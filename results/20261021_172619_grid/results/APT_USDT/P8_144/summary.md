# EMA Hourly Continuation — APT/USDT P8_144

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 1.0114 |
| net_win_rate | 0.5427 |
| gross_profit_factor | 1.1693 |
| gross_win_rate | 0.5427 |
| sharpe_ratio | 0.1149 |
| sortino_ratio | 0.0285 |
| max_drawdown | 0.1024 |
| cagr | 0.0066 |
| net_avg_win | 92.6516 |
| net_avg_loss | -108.6945 |
| avg_hold_time_bars | 58.5427 |
| exposure | 0.7797 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
