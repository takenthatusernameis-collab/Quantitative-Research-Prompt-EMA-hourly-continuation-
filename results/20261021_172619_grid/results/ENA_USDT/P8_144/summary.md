# EMA Hourly Continuation — ENA/USDT P8_144

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 1.0576 |
| net_win_rate | 0.5426 |
| gross_profit_factor | 1.1834 |
| gross_win_rate | 0.5426 |
| sharpe_ratio | 0.3765 |
| sortino_ratio | 0.1024 |
| max_drawdown | 0.1054 |
| cagr | 0.0382 |
| net_avg_win | 94.9195 |
| net_avg_loss | -106.4781 |
| avg_hold_time_bars | 45.1761 |
| exposure | 0.7228 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
