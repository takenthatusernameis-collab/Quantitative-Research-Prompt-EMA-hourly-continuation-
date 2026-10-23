# EMA Hourly Continuation — GMT/USDT P12_144

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7207 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0028 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.9684 |
| sortino_ratio | -0.5382 |
| max_drawdown | 0.5020 |
| cagr | -0.2247 |
| net_avg_win | 65.5273 |
| net_avg_loss | -90.4337 |
| avg_hold_time_bars | 43.1260 |
| exposure | 0.7312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
