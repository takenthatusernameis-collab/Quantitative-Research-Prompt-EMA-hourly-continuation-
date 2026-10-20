# EMA Hourly Continuation — T/USDT P8_144

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6952 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 1.0363 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.7289 |
| sortino_ratio | -0.7971 |
| max_drawdown | 0.6609 |
| cagr | -0.3186 |
| net_avg_win | 67.0382 |
| net_avg_loss | -91.2362 |
| avg_hold_time_bars | 36.6889 |
| exposure | 0.7205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
